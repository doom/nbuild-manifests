#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import shutil
import stdlib
from stdlib.template import basic
from stdlib.manifest import manifest
from stdlib.split.drain_all import drain_all_with_doc


def install_rust():
    build = stdlib.build.current_build()

    stdlib.cmd(f'''./install.sh             \
        --destdir={build.install_cache}/    \
        --prefix=/usr/                      \
    ''')

    with stdlib.pushd(build.install_cache):
        shutil.move('usr/etc/', 'etc/')


@manifest(
    name='rust',
    category='dev-lang',
    description='''
    A language empowering everyone to build reliable and efficient software.
    ''',
    tags=['rust', 'cargo', 'system', 'language'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.APACHE, stdlib.license.License.MIT],
    upstream_url='https://www.rust-lang.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.41.0',  # TODO: Point to stable Rust instead
            'fetch': [{
                'url': 'https://static.rust-lang.org/dist/rust-nightly-x86_64-unknown-linux-gnu.tar.gz',
                'sha256': '37c557e58e34455b78134b8d5e0ae7311848f5e6d9d542f451c1945cdc66ac56',  # TODO: This sha isn't useful, as this is a nightly build
            }]
        },
    ],
)
def build(build):
    packages = basic.build(
        install=install_rust,
        split=drain_all_with_doc,
    )

    packages['dev-lang/rust'].requires('dev-apps/gcc')
    packages['dev-lang/rust'].requires('dev-apps/binutils')

    return packages
