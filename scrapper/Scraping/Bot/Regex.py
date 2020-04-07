import re

def reg (mache,text):

    pattern = re.compile(mache)
    matches = pattern.finditer(text)
    boundary = ()

    for match in matches:
        boundary = match.span()
        print(match, matches)
    return boundary
