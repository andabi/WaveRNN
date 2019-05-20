# -*- coding: utf-8 -*-
#!/usr/bin/env python

""""""

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))


def get_requirements(filename='requirements.txt'):
    deps = []
    with open(filename, 'r') as f:
        for pkg in f.readlines():
            if pkg.strip():
                deps.append(pkg)
    return deps


setup(
    name='wave_rnn',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
)
