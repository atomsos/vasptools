#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='vasptools',
    version="0.2.0", 
    description=(
        'tool collection for parsing vasp inputs & outputs'
    ),
    long_description=open('README.rst').read(),
    author='Sky Zhang',
    author_email='sky.atomse@gmail.com',
    maintainer='Sky Zhang',
    maintainer_email='sky.atomse@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/atomse/vasptools',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'sh>=1.10.0',
    ]
)

