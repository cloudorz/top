from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='top',
      version=version,
      description="Taobao open platform API",
      long_description="""\
Taobao open platform API""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='cloud',
      author_email='cloudcry@gmail.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
