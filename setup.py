import sys
from setuptools import setup, find_packages

setup(
    name = "cubes-ga",
    version = '0.1',

    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
    ],

    entry_points={
    },

    test_suite = "tests",

    author = "Stefan Urbanek",
    author_email = "stefan.urbanek@gmail.com",
    description = "Google Analytics backend for the Cubes Python OLAP library",
    license = "MIT",
    keywords = "olap multidimensional data analysis",
    url = "http://cubes.databrewery.org"
)

