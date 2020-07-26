# Note:
# - the function converts only 4 old-style emojis to unicode emojis, and it
#   doesn't take into account variaces such as `: )`

def convert_emj(s):
    
    d = {':)': '\U0001F600',
         ';)': '\U0001F609',
         ':P': '\U0001F61B',
         ';P': '\U0001F61C'}
    
    s_in = list(s)
    s_out = s_in[:]
    for i in range(len(s_in) - 1):  # skip last item to avoid slicing error
        tmp = s_in[i] + s_in[i+1]
        if tmp in d:
            s_out[i] = d[tmp]
            s_out[i+1] = ''
        
    return ''.join(s_out)

text = "Hey, dude!:) Wanna grab some beers? ;P"
print(text, '\n', convert_emj(text))