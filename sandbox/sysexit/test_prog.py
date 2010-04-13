#!/usr/bin/env python
"""

"""
import sys

def test_sysexit():
    try:
        raise AttributeError
    except:
        print "You're inside the except block now.\n\n"
        sys.exit()
    finally:
        print "And now in the finally block"
        sys.exit()
        print "this should not print"
    

if __name__ == '__main__':
    test_sysexit()
