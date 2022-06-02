import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="peridot",
    version="0.0.1",
    author="Hayden Young",
    author_email="hayden@hbjy.dev",
    description="A Python API library to Peridot, the RESF build system.",

    license="Apache-2.0",
    keywords="peridot resf api library",
    url="http://packages.python.org/peridot.py",
    packages=['peridot'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache-2.0",
    ],

    install_requires=[
        "requests",
    ],
)
