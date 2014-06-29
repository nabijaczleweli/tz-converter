"""

Contains getters for cities in a specific region.

"""
import sys
sys.path.append(u'usr/share/tz-converter/lib')

import pytz
import re

def get_global_timezone_list():
    return pytz.common_timezones


def get_africa_timezone_list():
    africa_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Africa", city):
            africa_timezone_list.append(city)
    return africa_timezone_list


def get_america_timezone_list():
    america_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^America", city):
            america_timezone_list.append(city)
    return america_timezone_list


def get_asia_timezone_list():
    asia_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Asia", city):
            asia_timezone_list.append(city)
    return asia_timezone_list


def get_australia_timezone_list():
    australia_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Australia", city):
            australia_timezone_list.append(city)
    return australia_timezone_list


def get_europe_timezone_list():
    europe_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Europe", city):
            europe_timezone_list.append(city)
    return europe_timezone_list


def get_pacific_timezone_list():
    pacific_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Pacific", city):
            pacific_timezone_list.append(city)
    return pacific_timezone_list


def get_us_timezone_list():
    us_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^US", city):
            us_timezone_list.append(city)
    return us_timezone_list