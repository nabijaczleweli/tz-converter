from setuptools import setup
#from distutils.core import setup
import os


def gen_data_files(*dirs):
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            results.append((root, map(lambda f: root + "/" + f, files)))
    return results


setup(name='tz-converter',
      version='1.0.0-1',
      description="An application for converting the time across time zones",
      author='David Maiorino (Dave)',
      author_email='maiorinodavid@gmail.com',
      url='https://github.com/DMaiorino/tz-converter',
      license='GPL-3+',
      keywords='productivity',
      scripts=["tz-converter", "main_widget.py", "timezone_info.py"],
      )
