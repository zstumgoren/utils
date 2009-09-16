#!/usr/bin/env python
"""
This script cleans gobbledygook characters from xml/HTML source files.

It relies in part on Fredrik Lundh's strip_html function:
    http://effbot.org/zone/re-sub.htm
Sample Usage:
    import codecs
    from feedcleaner import strip_html, translate_code
    
    # open outfile with utf-8 encoding 
    outfile = codecs.open('data_out.txt','wb','utf-8')
    
    for line in open('src_data.txt','rb'):
        newline = process(line)
        
        # Check if line exists (process function strips blank lines)
        if newline:
            outline = newline + '\n'
            outfile.write(outline)
"""

import re
import htmlentitydefs

def translate_code(text):
    text = text.replace("&#145;","'") 
    text = text.replace("&#146;","'")
    text = text.replace("&#147;",'"')
    text = text.replace("&#148;",'"')
    #text = text.replace("&#149;","")  #is a bullet point 
    text = text.replace("&#150;","-") 
    text = text.replace("&#151;","--")
    return text

# Removes HTML markup from a text string
# @param text The HTML source.
# @return The plain text.  If the HTML source contains non-ASCII
#     entities or character references, this is a Unicode string.

def strip_html(text):

    def fixup(m):
        text = m.group(0)
        if text[:1] == "<":
            return "" # ignore tags
        if text[:2] == "&#":
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        elif text[:1] == "&":
            import htmlentitydefs
            entity = htmlentitydefs.entitydefs.get(text[1:-1])
            if entity:
                if entity[:2] == "&#":
                    try:
                        return unichr(int(entity[2:-1]))
                    except ValueError:
                        pass
                else:
                    return unicode(entity, "iso-8859-1")
        return text # leave as is
    return re.sub("(?s)<[^>]*>|&#?\w+;", fixup, text)

# Removes HTML or XML character references and entities from a text string.
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.

def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

def process(line):
    try:
        outline = strip_html(translate_code(line)).strip()
    except:
        outline = "ERROR -- %s" % line
    return outline
