#!/usr/bin/env python
# -*- coding: utf-8 -*-

import a
from setuptools import setup, find_packages

setup(name='a',
      version=a.__version__,
      description=a.__desc__,
      author=a.__author__,
      author_email=a.__author_email__,
      url=a.__url__,
      packages=find_packages())
