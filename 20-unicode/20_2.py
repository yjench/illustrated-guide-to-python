# Note:
# - the function only turns ascii letters upside down; it does not flip digits,
#   punctuation, etc
# - in extended latin unicode blocks, unicode names for inverted letters w.o. 
#   head-tail symmetry can be formed by adding "TURNED" to names of original
#   letters: https://stackoverflow.com/questions/2995340/how-does-uʍop-ǝpᴉsdn-text-work
# - as not all flipped uppercase letters can be found in these blocks, they are
#   converted to lowercase
# - `unicodedata` module: https://docs.python.org/3/library/unicodedata.html
#   , and its usage: https://docs.python.org/3/howto/unicode.html

import string
import unicodedata

def turn_letters(s):
    result = []
    for c in s.lower():
        c_rev = c
        
        if c in string.ascii_letters:
            name = unicodedata.name(c)
            name_rev = name[:-1] + 'TURNED ' + name[-1:]
                        
            try:
                c_rev = unicodedata.lookup(name_rev)
              
            except KeyError: # no turned chars for letters with head-tail symmetry
                pass
        
        result.append(c_rev)
    return ''.join(result)

print(turn_letters("When is corona gonna be over?"))