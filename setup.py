#!/usr/bin/env python
# coding: utf-8
'''
TOP-python
--------
Taobao open platform API SDK.
--------
next, make more OIM
'''

from setuptools import setup
setup(
    name='top',
    version='0.1',
    url='https://github.com/cloudcry/top',
    license='BSD',
    author='cloud',
    author_email='cloudcry@gmail.com',
    description='python TOP API SDK',
    long_description=__doc__,
    packages=['top'],
    namespace_packages=['top'],
    #test_suite='unittest',
    zip_safe=False,
    platforms='any',
    #install_requires=[],
    #tests_require=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
