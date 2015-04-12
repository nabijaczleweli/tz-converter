from setuptools import setup
import os


def gen_data_files(*dirs):
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            results.append((root, map(lambda f: root + "/" + f, files)))
    return results


setup(name='tz-converter',
      version='1.0.0',
      description="Tool for converting the time across time zones",
      long_description=("Convert the time and date across time zones\n"
                        "This tool provides a simple interface for converting the time and\n"
                        "date between two time zones. Written in Python3 and using Pyside,\n"
                        "this interface allows the user to save a certain time zone and\n"
                        "restore it after further changes. The timezone information is\n"
                        "taken from pytz, supplying seven different regions: Africa,\n"
                        "America, Asia, Australia, Europe, Pacific, and US."),
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
                  ('/usr/share/doc/tz-converter', ['AUTHORS',
                                                   'changelog.Debian.gz',
                                                   'debian/copyright']),
                  ],
      classifiers=['Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3',
                   'Intended Audience :: End Users/Desktop',
                  ]
      )
