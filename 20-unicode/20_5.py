# Note:
# - the function converts only 4 old-style emojis to unicode emojis, and it
#   doesn't take into account variaces such as `: )`

def convert_emj(text):
    
    d = {':)': '\U0001F600',
         ';)': '\U0001F609',
         ':P': '\U0001F61B',
         ';P': '\U0001F61C'}
    
    s = list(text)
    for i in range(len(s) - 1):  # exclude last item
        tmp = s[i] + s[i+1]
        if tmp in d:
            s[i], s[i+1] = d[tmp], ''
        
    return ''.join(s)

text = "Hey, dude!:) Wanna grab some beers? ;P"
print(text, '\n', convert_emj(text))