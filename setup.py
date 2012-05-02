from setuptools import setup, find_packages
import os

version = '1.0.10'

setup(name='mfabrik.webandmobile',
      version=version,
      description="Mobile and multichannel content management for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone cms multichannel mobile publishing app applications iphone android nokia blackberry',
      author='mFabrik Research Oy',
      author_email='research@mfabrik.com',
      url='http://webandmobile.mfabrik.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['mfabrik'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pywurfl==6.4.1b',          
          'mobile.sniffer==1.0.0',
          'mobile.heurestics==0.9',
          'mobile.htmlprocessing==1.0.0',
          'mfabrik.behaviorutilities==0.1.1',
          'gomobile.mobile==1.0.4',
          'gomobile.convergence==1.0.2',
          'gomobile.supporter==0.9.3',
          'gomobiletheme.basic==1.0.3',
          'gomobile.imageinfo==0.9.1',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
