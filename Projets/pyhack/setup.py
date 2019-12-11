#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from setuptools import setup
import pyhack

long_description = open("README.md").read()

setup(
    name="pyhack",
    version=pyhack.__version__,
    description="pyhack game in the terminal",
    long_description=long_description,
    license=pyhack.__licence__,
    author=pyhack.__author__,
    author_email="nicolas.vincent100@gmail.com",
    url="https://github.com/NicovincX2/Ensimag/tree/master/Projets/pyhack",
    install_requires="numpy",
    python_requires=">=3.6",
    packages=["pyhack"],
    test_suite="tests",
)
