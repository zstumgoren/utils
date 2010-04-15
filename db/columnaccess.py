#!/usr/bin/env python


class RowWrapper(object):
    """
    This class wraps result rows from a database query, 
    so that you can more easily access individual row values 
    by column name. 
    """
    def __init__(self, cursor, row):
        for (attr, val) in zip((d[0] for d in cursor.description), row):
            setattr(self, attr, val)
