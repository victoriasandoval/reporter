from setuptools import setup
from setuptools import find_packages


DISTNAME = "reporter"

MAJOR = 0
MINOR = 0
MICRO = 1
ISRELEASED = False
VERSION = f"{MAJOR}.{MINOR}.{MICRO}"


setup(name=DISTNAME, version=VERSION, packages=find_packages(), zip_safe=False)
