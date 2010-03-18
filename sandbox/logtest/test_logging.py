#!/usr/bin/env python
"""
  Fiddling around with logging module:
    http://docs.python.org/library/logging.html
"""
import logging
import sys

LOG_FILE = 'script_activity.log'
logging.basicConfig(filename=LOG_FILE,level=logging.INFO)

def test_logger():
    try:
        logging.info('Test normal logging message')
        raise ValueError 
    except Exception:
        msg = 'test exception logging'
        #FORMAT = filename, line #, function name error
        logging.exception(msg)# ,format=FORMAT)

if __name__ == '__main__':
    sys.exit(test_logger())
