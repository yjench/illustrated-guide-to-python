import string
from collections import Counter

text = '''
To go into solitude, a man needs to retire as much from his chamber as from society. I am not solitary whilst I read and write, though nobody is with me. But if a man would be alone, let him look at the stars. The rays that come from those heavenly worlds, will separate between him and what he touches. One might think the atmosphere was made transparent with this design, to give man, in the heavenly bodies, the perpetual presence of the sublime. Seen in the streets of cities, how great they are! If the stars should appear one night in a thousand years, how would men believe and adore; and preserve for many generations the remembrance of the city of God which had been shown! But every night come out these envoys of beauty, and light the universe with their admonishing smile.
'''

table = str.maketrans({key: None for key in string.punctuation})
words = text.translate(table).lower().split()

# Method 1: standard for loop
counter1 = {}
for word in words:
    if word not in counter1:
        counter1[word] = 1
    else:
        counter1[word] += 1
        
# Method 2: Counter dict
counter2 = Counter(words)

assert counter1 == counter2, '2 methods give different solutions'
print(counter1)