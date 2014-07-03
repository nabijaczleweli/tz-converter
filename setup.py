from setuptools import setup
import os

def gen_data_files(*dirs):
    results = []
    for src_dir in dirs:
        for root,dirs,files in os.walk(src_dir):
            results.append((root, map(lambda f:root + "/" + f, files)))
    return results


setup(name='tz-converter',
      version='1.0.0',
      description="An application for converting the time across time zones",
      author='David Maiorino (Dave)',
      author_email='maiorinodavid@gmail.com',
      url='https://github.com/DMaiorino/tz-converter',
      license='GNU',
      keywords='productivity',
      scripts = ["tz-converter", "main_widget.py", "timezone_info.py"],
      data_files = gen_data_files("lib", "icons"),
      install_requires=['PySide', 'DateTime']
      )
