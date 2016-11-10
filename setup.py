#!/usr/bin/env python
# Copyright (c) Aaron Gallagher <_@habnab.it>
# See COPYING for details.

import io
from setuptools import setup


with io.open('README.rst', mode='r', encoding='utf8') as infile:
    LONG_DESCRIPTION = infile.read()

with io.open('requirements.txt', mode='r', encoding='utf8') as infile:
    INSTALL_REQUIRES = infile.read().split()

setup(
    name='txsocksx',
    description='Twisted client endpoints for SOCKS{4,4a,5}',
    long_description=LONG_DESCRIPTION,
    author='Aaron Gallagher',
    author_email='_@habnab.it',
    url='https://github.com/habnabit/txsocksx',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Internet',
    ],
    license='ISC',

    setup_requires=['vcversioner>=1'],
    vcversioner={
        'version_module_paths': ['txsocksx/_version.py'],
    },
    install_requires=INSTALL_REQUIRES,
    packages=['txsocksx', 'txsocksx.test'],
)
