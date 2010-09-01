#!/usr/bin/env python
"""
 Utility function for generating SQL statements
"""

def create_insert_sql(table, **params):
    """
    Returns SQL insert statement for a given table and dict of params.
    >>> table = 'candidates'
    >>> params = {'name':'John Smith', 'age':40, 'employer':"Smith's Engineering"}
    >>> sql = create_insert_sql(table, **params)
    >>> print sql
    INSERT INTO candidates (age, employer, name) VALUES ('40', 'Smith''s Engineering', 'John Smith');
    
    """
    SQL = "INSERT INTO %(table)s (%(columns)s) VALUES (%(params)s);"
    columns = ", ".join(sorted(params.keys()))
    # escape single quotes inside a quoted field

    clean_params = ", ".join(["'%s'" % str(field).replace("'","''") 
                              for field in sorted_dict_values(params)])
    return SQL % {'table':table, 'columns':columns, 'params':clean_params}

def sorted_dict_values(adict):
    """
    Dictionary sort courtesy of Alex Martelli:
    http://code.activestate.com/recipes/52306-to-sort-a-dictionary/
    """
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
