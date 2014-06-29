from setuptools import setup, find_packages 

setup(name='tz-converter',
      version='1.0.0',
      description="An application for converting the time across time zones",
      author='David Maiorino (Dave)',
      author_email='maiorinodavid@gmail.com',
      url='https://github.com/DMaiorino/tz-converter',
      license='GNU',
      keywords='productivity',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      install_requires=['PySide', 'Delorean', 'tzlocal','DateTime']
      )
