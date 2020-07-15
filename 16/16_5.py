import string
from collections import defaultdict

paragraph = '''
You listen to sea in silent. Seen in the streets of cities, how great they are!
 If the stars should appear one night in a thousand years, how would men believe
 and adore. And restful is not fluster. This paragraph is going to contain 
 anagrams. There is an arc through which you can drive a car quickly. That ant 
 has a tan face. I have tons of snot fo you. And then ouch said the chou man. 
 I hit the ram in his arm pit"""
'''

table = str.maketrans({key: None for key in string.punctuation})
words = set(paragraph.translate(table).lower().split())  # only unique words

anagrams = defaultdict(list)
for word in words:
    word_sorted = ''.join(sorted(word))  # key as sorted string of letters
    anagrams[word_sorted].append(word)

print('Anagrams found:')
print('-'*30)
for k, v in anagrams.items():
    if len(v) > 1:
        print(f'{k}: {v}')