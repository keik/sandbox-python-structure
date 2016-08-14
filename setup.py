#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sandbox_python_structure
from setuptools import setup, find_packages

setup(name='sandbox-python-structure',
      version=sandbox_python_structure.__version__,
      description=sandbox_python_structure.__desc__,
      author=sandbox_python_structure.__author__,
      author_email=sandbox_python_structure.__author_email__,
      url=sandbox_python_structure.__url__,
      packages=find_packages())
