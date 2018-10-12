from setuptools import setup

setup(name='pets',
      version='0.1',
      description='pets example',
      author='Siwei Wang',
      author_email='example@example.com',
      packages=['pets'],
      entry_points={
          'console_scripts': [
              'run=runner:main',
          ],
      },
      )

__author__ = 'Siwei Wang'
