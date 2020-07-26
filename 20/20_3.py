import encodings

def check_available_encodings(s):
    e_list = []
    for e in encodings.aliases.aliases:
        try:
            s.encode(e)
            e_list.append(e)
            
        except LookupError:  # some are not text-to-byte encodings
            pass
        
        except UnicodeEncodeError:  # some can't represent all input chars
            pass
        
    return e_list

name_turned = 'ʎᴉ-jǝn'
print(f'Unicode string: {name_turned}')
print('Available encodings:\n', check_available_encodings(name_turned))