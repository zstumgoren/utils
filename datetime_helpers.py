#!/usr/bin/env python
"""
Various functions used to aid in date and time-based calculations
"""
from time import asctime
from datetime import datetime, timedelta

def get_date_string(date_obj=datetime.now(), format="%Y-%m-%d"):
    """
    Accepts a datetime object and an optional format parameter
    Usage:
        get_date_string(format="%Y%m%dT%H%M%S")
    """
    return datetime.strftime(date_obj, format)
        
def window():
    """
    This variable accounts for weekends in the efilings SQL queries. 
    It returns a "4" on Mondays and a "2" otherwise." Used by, among others,
    the fec.models Parser classes to adjust their get_filings methods
    based on the day of the week.
    """
    if asctime().startswith('Mon'):
        return 4
    else:
        return 2
