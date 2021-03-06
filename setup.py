# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

with open('docs/requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='tango-happenings',
    version='0.7.2',
    author=u'Tim Baxter',
    author_email='mail.baxter@gmail.com',
    url='https://github.com/tBaxter/django-happenings',
    license='LICENSE',
    description='Reusable Django events and calendaring.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=required,
    zip_safe=False,
    include_package_data=True,
    dependency_links = [
        'http://github.com/tBaxter/vobject/tarball/master#egg=vobject',
    ]
)
