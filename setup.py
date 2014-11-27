#!/usr/bin/python3

from setuptools import setup
from setuptools import find_packages
import sys

setup(
        name='pywinamp',
        version='0.3',
        author='Yaron Inger, Arthur Jaron',
        author_email="arthurjaron@gmx.de",
        url="https://bitbucket.org/freeo/pywinamp",
        description='''Interface to Winamp API''',
        packages=find_packages(),
        )
