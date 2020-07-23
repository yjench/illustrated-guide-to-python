import encodings

def check_available_encodings(s):
    e_list = []
    for e in encodings.aliases.aliases.keys():
        try:
            s.encode(e)
            e_list.append(e)
        except LookupError:  # some are not text encodings
            pass
        
        except UnicodeEncodeError:  # some can't represent all input chars
            pass
        
    return e_list

name_turned = 'Yᴉ-Jǝn'
print(f'Unicode string: {name_turned}')
print('Available encodings:')
print(check_available_encodings(name_turned))