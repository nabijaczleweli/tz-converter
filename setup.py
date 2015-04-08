from setuptools import setup
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
      scripts=["scripts/tz-converter"],
      packages=["tz_converter"],
      data_files=[('/usr/share/tz-converter/icons', ['tz_converter/data/icons/gnome-set-time.png', 
                                                     'tz_converter/data/icons/Saki-NuoveXT-Apps-world-clock.ico']),
                  ('/usr/share/man/man1/', ['tz_converter/data/manpages/tz-converter.1']),
                  ]
      )
