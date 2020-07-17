# Method 1: standard for loop
def convert_case1(string, separator='_'):
    
    words = list(string)
    for idx, char in enumerate(words):
        if idx > 0 and char.isupper():
            words[idx] = separator + char
    
    return ''.join(words).lower()

# Method 2: list comprehension
def convert_case2(string, separator='_'):
    l = [separator + c if c.isupper() else c for c in string]
    return ''.join(l).lower()[1:]

# Tests
string = "CapitalizedWords"
print(convert_case1(string), convert_case1(string, separator='-'))
print(convert_case2(string), convert_case2(string, separator='-'))