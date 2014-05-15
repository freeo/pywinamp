#!/usr/bin/python2

from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
import sys
# from cx_Freeze import setup, Executable

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

# Dependencies are automatically detected, but it might need fine tuning.
# build_exe_option = {"packages": ["os"], "excludes": ["tkinter"]}
# build_exe_options = {"include_files": [("DateCalc/preise.ini", "preise.ini")]}

setup(
        name='pywinamp',
        version='0.3',
        author='Yaron Inger, Arthur Jaron',
        author_email="arthurjaron@gmx.de",
        url="http://ingeration.blogspot.com",
        description='''Interface to Winamp API''',
        packages=find_packages(),
        tests_require=['pytest'],
        cmdclass = {'test': PyTest},
        # options = {"build_exe": build_exe_options},
        # executables = [Executable("DateCalc/zeitrechner.py", targetName = "Zeitrechner.exe", icon = "assets/pplogo.ico")]
        )

# http://peak.telecommunity.com/DevCenter/setuptools#test
# Abstract example for setting test_suite:
# test_suite = "my_package.tests.test_all"
# If the named suite is a package, any submodules and subpackages are
# recursively added to the overall test suite.
