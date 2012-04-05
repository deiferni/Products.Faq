from setuptools import setup, find_packages
import os

version = '1.1.3dev'

setup(name='Products.Faq',
      version=version,
      description="FAQ - An AT contenttype for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        ],
      keywords='FAQ Archetypes Plone Contenttype',
      author='Four Digits',
      author_email='info@fourdigits.nl',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
          'test': ['plone.app.testing']
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
