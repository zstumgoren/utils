import os
import sys
from xml.sax.handler import ContentHandler
import xml.sax

class countHandler(ContentHandler):
    def __init__(self):
        self.tags = {}
    
    def startElement(self, name, attr):
        if not self.tags.has_key(name):
            self.tags[name] = 0
        self.tags[name] += 1

        
def main():
    basepath = os.path.abspath(".")
    #inputfile = basepath+ "\\" + "report-pacprofile.xml"
    inputfile = sys.argv[1]
    parser = xml.sax.make_parser()
    handler = countHandler()
    parser.setContentHandler(handler)
    parser.parse(inputfile)
    tags = handler.tags.keys()
    tags.sort()
    
    for tag in tags:
        print tag, handler.tags[tag]

if __name__ == "__main__":
    main()