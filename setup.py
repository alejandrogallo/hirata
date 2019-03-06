# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.md') as fd:
    long_description = fd.read()

setup(
    name='hirata',
    version='0.1.0',
    author='Alejandro Gallo',
    author_email='aamsgallo@gmail.com',
    url='https://github.com/alejandrogallo/hirata',
    install_requires=[],
    long_description=long_description,
    keywords=[],
    entry_points=dict(
        console_scripts=[
            'hirata=hirata.main:main'
        ]
    ),
)
