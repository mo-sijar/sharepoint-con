#!/usr/bin/env python

import setuptools

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(name='sharepointing',
      version='0.1.4',
      description='A package to establish a connection to SharePoint site, and upload files through that connection',
      author='Mo Sijarrey',
      author_email='mo.sijar@gmail.com',
      url='https://github.com/mo-sijar/sharepointing',
      install_requires=REQUIREMENTS
     )
