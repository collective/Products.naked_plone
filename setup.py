from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='Products.naked_plone',
      version=version,
      description="An installable theme for Plone 3.0 that does little but override default public stylesheets with empty ones.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='https://svn.plone.org/svn/collective/Products.naked_plone/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
