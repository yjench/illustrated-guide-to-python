# Remove punctuation:
# 1 - for loop + conditional
# 2 - re module
# 3 - str.translate(table) + string module
#
# https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string

shakespeare = ''''Tis sweet and commendable in your nature, Hamlet,
To give these mourning duties to your father:
But, you must know, your father lost a father;
That father lost, lost his, and the survivor bound
In filial obligation for some term
To do obsequious sorrow: but to persever
In obstinate condolement is a course
Of impious stubbornness; 'tis unmanly grief;
It shows a will most incorrect to heaven,
A heart unfortified, a mind impatient,
An understanding simple and unschool'd:
For what we know must be and is as common
As any the most vulgar thing to sense,
Why should we in our peevish opposition
Take it to heart? Fie! 'tis a fault to heaven,
A fault against the dead, a fault to nature,
To reason most absurd: whose common theme
Is death of fathers, and who still hath cried,
From the first corse till he that died to-day,
'This must be so.' We pray you, throw to earth
This unprevailing woe, and think of us
As of a father: for let the world take note,
You are the most immediate to our throne;
And with no less nobility of love
Than that which dearest father bears his son,
Do I impart toward you. For your intent
In going back to school in Wittenberg,
It is most retrograde to our desire:
And we beseech you, bend you to remain
Here, in the cheer and comfort of our eye,
Our chiefest courtier, cousin, and our son.'''

emerson = '''To go into solitude, a man needs to retire as much from his
chamber as from society. I am not solitary whilst I read and write, though 
nobody is with me. But if a man would be alone, let him look at the stars. 
The rays that come from those heavenly worlds, will separate between him and 
what he touches. One might think the atmosphere was made transparent with this
 design, to give man, in the heavenly bodies, the perpetual presence of the 
 sublime. Seen in the streets of cities, how great they are! If the stars 
 should appear one night in a thousand years, how would men believe and adore;
 and preserve for many generations the remembrance of the city of God which 
 had been shown! But every night come out these envoys of beauty, and light 
 the universe with their admonishing smile.'''

import string

# Strip punctuation from strings
table = str.maketrans({key: None for key in string.punctuation})
shakespeare = shakespeare.translate(table)
emerson = emerson.translate(table)

# Transform strings to sets of lower-case words
shake_set = set(shakespeare.lower().split())
emer_set = set(emerson.lower().split())

# Check common and unique words
common_words = shake_set & emer_set
print(f'Common words:\n {common_words}\n')

unique_words = shake_set ^ emer_set
print(f'Uniques words:\n {unique_words}')
