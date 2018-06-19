#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='minecraft',
    version='1.0',
    description="",
    author="Ash Arnold",
    author_email='ash@dragonpaw.org',
    url='',
    packages=find_packages(),
    package_data={'minecraft': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
