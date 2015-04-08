#!/usr/bin/python3

"""

Contains getters for cities in a specific region.

"""
import sys
import os
import pytz
import re
real_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(u'%s/lib' % real_path)


def get_global_timezone_list():
    return pytz.common_timezones


def get_africa_timezone_list():
    africa_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Africa/\w+$", city):
            africa_timezone_list.append(city.split('/')[1])
    return africa_timezone_list


def get_america_timezone_list():
    america_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^America/\w+$", city):
            america_timezone_list.append(city.split('/')[1])
    return america_timezone_list


def get_asia_timezone_list():
    asia_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Asia/\w+$", city):
            asia_timezone_list.append(city.split('/')[1])
    return asia_timezone_list


def get_australia_timezone_list():
    australia_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Australia/\w+$", city):
            australia_timezone_list.append(city.split('/')[1])
    return australia_timezone_list


def get_europe_timezone_list():
    europe_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Europe/\w+$", city):
            europe_timezone_list.append(city.split('/')[1])
    return europe_timezone_list


def get_pacific_timezone_list():
    pacific_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^Pacific/\w+$", city):
            pacific_timezone_list.append(city.split('/')[1])
    return pacific_timezone_list


def get_us_timezone_list():
    us_timezone_list = []
    for city in pytz.common_timezones:
        if re.match("^US/\w+$", city):
            us_timezone_list.append(city.split('/')[1])
    return us_timezone_list


def get_city_region(current_city):

    for city in pytz.common_timezones:
        if re.match("^Africa", city) and current_city in city:
            return "Africa"
        if re.match("^America", city) and current_city in city:
            return "America"
        if re.match("^Asia", city) and current_city in city:
            return "Asia"
        if re.match("^Australia", city) and current_city in city:
            return "Australia"
        if re.match("^Europe", city) and current_city in city:
            return "Europe"
        if re.match("^Pacific", city) and current_city in city:
            return "Pacific"
        if re.match("^US", city) and current_city in city:
            return "US"

    return None
