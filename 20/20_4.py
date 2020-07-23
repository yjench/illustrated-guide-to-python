def convert_quotes(s_ascii):
    count = 0
    s = ""
    for c in s_ascii:
        if c == '"':
            if count % 2:
                c = '\N{LEFT DOUBLE QUOTATION MARK}'
                print('left')
            else:
                c = '\N{RIGHT DOUBLE QUOTATION MARK}'
                print('right')
            
            count += 1
            
        s += c
    
    return s

print('Python comes with "Batteries included".')
print(convert_quotes('Python comes with "Batteries included".'))