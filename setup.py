from setuptools import setup, find_packages
import sys, os

version = '2'

setup(name='django_google_analytics',
      version=1,
      description="Google analytics web property per site in django admin",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django google analytics site',
      author='Benjamin Wilbur',
      author_email='wilburb@wilburweb.com',
      url='wilburweb.com',
      license='GNU General Public License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      package_data={
        'analytics': [
            'templates/analytics/*.html',
        ],
      },
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
