#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, 'README.rst')) as f:
    readme = f.read()

with open(os.path.join(base_dir, 'HISTORY.rst')) as f:
    history = f.read()

about = {}
with open(os.path.join(base_dir, 'besttags', '__about__.py')) as f:
    exec(f.read(), about)

setup(
    name='besttags',
    description="Get the best hashtags for your post",
    version=about['__version__'],
    url='https://github.com/axju/besttags',

    author=about['__author__'],
    author_email=about['__email__'],

    license="MIT license",
    keywords='besttags',

    long_description=readme + '\n\n' + history,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    install_requires=[
        'requests',
        'bs4',
    ],

    entry_points={
        'console_scripts': [
            'best-tags=besttags.__main__:main',
        ],
    },

    zip_safe=False,
    include_package_data=True,
    packages=find_packages(include=['besttags']),

    test_suite='tests',
)
