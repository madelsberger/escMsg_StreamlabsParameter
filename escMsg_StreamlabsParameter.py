import urllib
import re

ScriptName = "escMsg"
Website = "https://github.com/madelsberger/escMsg_StreamlabsParameter"
Description = "'escaped' $msg parameter - $escMsg ; $escMsg(<esc-type>)"
Creator = "madelsberger"
Version = "1.0.0"

def Init():
    pass

def Parse(parseString, user, target, message):
    old = parseString
    new = ""
    pattern = "(.*)\$escMsg(?:\s*\(\s*([a-zA-Z0-9_]+)\s*\))?(.*)"
    match = re.match(pattern, old)
    while match is not None:
        new += match.group(1)

        if match.group(2) is None:
            new += escPython(message)
        elif match.group(2).lower() == "html":
            new += escHtml(message)
        elif match.group(2).lower() == "url":
            new += urlEncode(message)

        old = match.group(3)
        match = re.match(pattern, old)
    else:
        new += old
    return new

def escPython(m):
    m = re.sub('\\\\', '\\\\', m)
    m = re.sub('\'', '\\\\\'', m)
    m = re.sub('"', '\\"', m)
    return m

def escHtml(m):
    m = re.sub('&', '&amp;', m)
    m = re.sub('<', '&lt;', m)
    m = re.sub('>', '&gt;', m)
    m = re.sub(' ', '&nbsp;', m)
    m = re.sub('"', '&#34;', m)
    m = re.sub('\'', '&#39;', m)
    return m

def urlEncode(m):
    return urllib.quote_plus(m)
