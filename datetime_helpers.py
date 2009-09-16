!/usr/bin/env python
"""
This program contains various functions used to aid in 
date and time-based calculations
"""
from datetime import datetime
from time import asctime

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
