#!/usr/bin/env python

import setuptools

setuptools.setup(name='sharepointing',
      version='0.1.4',
      description='A package to establish a connection to SharePoint site, and upload files through that connection',
      author='Mo Sijarrey',
      author_email='mo.sijar@gmail.com',
      url='https://github.com/mo-sijar/sharepointing',
      install_packages=["Office365-REST-Python-Client>=2.3.16"]
     )
