#!/usr/bin/env python


class RowWrapper(object):
    """
    This class wraps result rows from a database query, 
    so that you can more easily access individual row values 
    by column name. 

    >>> from code.utils.db import RowWrapper 
    >>> class CursorMock(object):
    ...    def __init__(self):
    ...        self.description = [('form_type', 510, 510, 0, 0, 1),('district', 1021, 1021, 0, 0, 1),('cmte_id', 510, 510, 0, 0, 1),('committee', 510, 510, 0, 0, 1),]
    >>> curs = CursorMock()
    >>> for row in cursor.fetchall():
    ...     r = RowWrapper(cursor, row)
    ...     print r.committee, r.cmte_id, r.district
    ...     
    Paul McKain for Congress C00464255 FL-02
    Edward Gonzalez for Congress C00473983 CA-16
    """
    def __init__(self, cursor, row):
        for (attr, val) in zip((d[0] for d in cursor.description), row):
            setattr(self, attr, val)
