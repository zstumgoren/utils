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
    except ValueError:
        return value

def ordinal(value):
    """
    Converts a *postive* integer or its string representation
    to an ordinal value.

    >>> for i in range(1,13):
    ...     ordinal(i)
    ...     
    u'1st'
    u'2nd'
    u'3rd'
    u'4th'
    u'5th'
    u'6th'
    u'7th'
    u'8th'
    u'9th'
    u'10th'
    u'11th'
    u'12th'

    >>> for i in (100, '111', '112',1011):
    ...     ordinal(i)
    ...     
    u'100th'
    u'111th'
    u'112th'
    u'1011th'

    """
    try:
        value = int(value)
    except ValueError:
        return value

    if value % 100//10 != 1:
        if value % 10 == 1:
            ordval = u"%d%s" % (value, "st")
        elif value % 10 == 2:
            ordval = u"%d%s" % (value, "nd")
        elif value % 10 == 3:
            ordval = u"%d%s" % (value, "rd")
        else:
            ordval = u"%d%s" % (value, "th")
    else:
        ordval = u"%d%s" % (value, "th")

    return ordval

if __name__ == '__main__':
    import doctest
    doctest.testmod()
