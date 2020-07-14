import string

text = '''
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.
'''
table = str.maketrans({key: None for key in string.punctuation})
words = text.translate(table).lower().split()

# Method 1: dict + .setdefault
count1 = {}
for word in words:
    count1.setdefault(word, 0)
    count1[word] += 1

# Method 2: Counter
from collections import Counter
count2 = Counter(words)

# Check results
print(count1 == count2)
print()
print(count1)
