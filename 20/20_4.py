def convert_quotes(s_ascii):
    count = 0
    letters = []
    for c in s_ascii:
        if c == '"':
            c = ('\N{LEFT DOUBLE QUOTATION MARK}' if not count % 2 else
                 '\N{RIGHT DOUBLE QUOTATION MARK}')
            count += 1
            
        letters.append(c)

    return ''.join(letters)

s_ascii = 'Python comes with "Batteries included" - "AAA batteries".'
print(convert_quotes(s_ascii))