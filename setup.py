#!/usr/bin/env python
import os
from distutils.core import setup

setup(name='pype',
      version='0.1',
      description='Tiny helper for command-line python',
      long_description=open(os.path.join(os.path.dirname(__file__),
                                         'readme.md')).read(),
      author='jisaacstone',
      author_email='jisaacstone+python@gmail.com',
      license='MIT',
      url='https://github.com/jisaacstone/pype',
      scripts=['pype'],
      classifiers=["Development Status :: 3 - Alpha",
                   "Topic :: Utilities",
                   "License :: OSI Approved :: MIT License"],
     )
