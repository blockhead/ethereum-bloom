#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DIR = os.path.dirname(os.path.abspath(__file__))


from setuptools import setup, find_packages


readme = open(os.path.join(DIR, 'README.md')).read()


setup(
    name='ethereum-bloom',
    version="0.4.0",
    description="""Python implementation of the Ethereum Trie structure""",
    long_description=readme,
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/pipermerriam/ethereum-bloom',
    include_package_data=True,
    py_modules=['eth_bloom'],
    install_requires=[
        "pysha3>=0.3",
    ],
    license="MIT",
    zip_safe=False,
    keywords='ethereum blockchain evm trie merkle',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
