#!/usr/bin/env python
import argparse
import sys

p = argparse.ArgumentParser(prog=sys.argv[0],
                            formatter_class=argparse.RawTextHelpFormatter,
                            description="Sets execution mode") 

p.add_argument("-l", "--live", action="store_true", dest="live",
help="""Live mode enacts a series of policies, including:
* distributes email to full distribution list
* archives the email
* logs errors to a file
""")

p.add_argument("-d", "--debug", action="store_true", dest="debug",
help="""Debug mode toggles policies for testing purposes:
* only distribute Daily Query email to admin user
* logs to stdout/shell
* turns off email archiving
""")

mode = p.parse_args()
if mode.live:
    print "You have set the script to live mode"
    print "See?", mode
elif mode.debug:
    print "You have set the script to debuge mode"
    print "See?", mode
else:
    print "You did not set a program mode!"
