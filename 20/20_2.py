# -*- coding: utf-8 -*-
# 
# Note:
# - the function only turns ascii letters upside down; it does not flip digits,
#   punctuation, etc
# - `unicodedata` module: https://docs.python.org/3/library/unicodedata.html
#   , and its usage:  https://docs.python.org/3/howto/unicode.html
# - useful post: https://stackoverflow.com/questions/2995340/how-does-uʍop-ǝpᴉsdn-text-work

import string
import unicodedata

def turn_letters(s):
    result = []
    for c in s:
        c_reversed = c

        if c in string.ascii_letters:
            name = unicodedata.name(c)
            name_reversed = name[:-1] + 'TURNED ' + name[-1:]
            
            try:
                c_reversed = unicodedata.lookup(name_reversed)
              
            except KeyError: # no turned chars for letters with head-tail symmetry
                pass
        
        result.append(c_reversed)
    return ''.join(result)

print(turn_letters("When is corona gonna be over?"))