#!/usr/bin/env python
"""
A suite of functions to gussy up numbers and strings for human eyes.

Inspired by Django's humanize template filters:

http://code.djangoproject.com/browser/django/trunk/ \
    django/contrib/humanize/templatetags/humanize.py
"""
from decimal import Decimal
import locale
locale.setlocale(locale.LC_ALL,'')

def currency(value):
    """
    Convert numbers to currency format using locale settings
    """
    try:
        decval = Decimal(value)
        return locale.currency(decval, grouping=True)
    except TypeError:
        value

def ordinal(value):
    """
    Converts an integer to it's ordinal as a string.
    For example 1 to "1st", 2 to "2nd", 3 to "3rd", etc.
    """
    try:
        value = int(value)
    except ValueError:
        return value

    if value % 100/10 <> 1:
        if value % 10 == 1:
            ord = u"%d%s" % (value, "st")
            return ord 
        elif value % 10 == 2:
            ord = u"%d%s" % (value, "nd")
            return ord
        elif value % 10 == 3:
            ord = u"%d%s" % (value, "rd")
            return ord
        else:
            ord = u"%d%s" % (value, "th")
            return ord
    else:
        ord = u"%d%s" % (value, "th")
        return  ord
