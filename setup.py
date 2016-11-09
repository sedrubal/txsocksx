#!/usr/bin/env python
# Copyright (c) Aaron Gallagher <_@habnab.it>
# See COPYING for details.

from setuptools import setup


def get_requirements():
    """returns a list of all requirements"""
    requirements = []
    with open('requirements.txt', 'rb') as infile:
        for line in (l.decode('utf8').strip() for l in infile):
            if line and not line.startswith('#'):
                requirements.append(line)

    return requirements


with open('README.rst', 'rb') as infile:
    LONG_DESCRIPTION = infile.read().decode('utf8')


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
    install_requires=get_requirements(),
    packages=['txsocksx', 'txsocksx.test'],
)
