#!/usr/bin/env python

from distutils.core import setup

#long_desc = open('README.rst').read()

setup(name='hometemp',
    version='0.1.0',
    description='graph temp inside, outside, and target',
    #long_description=long_desc,
    packages=('hometemp',),
    license='BSD',
    author='Michael Hrivnak',
    author_email='mhrivnak@hrivnak.org',
    url='https://github.com/mhrivnak/hometemp',
    classifiers=(
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
        'Topic :: Home Automation',
    )
)
