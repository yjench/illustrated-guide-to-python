# Illustrated guide to python 3



## Ch 17

Prime numbers > 1



## Ch 16

**Mapping type: `dict`**

- Ref: https://docs.python.org/3/library/stdtypes.html#dict

```python
#d = {'k1': 1, 'k2': 2}
d = {'k1': 1, 'k2': 'a'}  # values: hete
d = {'k1': 1, 100: 2}  # keys: hete
#d = {'k1': 1, [1]: 2} # keys: hashable
d = {'k1': 1, 'k2': [1]}

d['k3'] = 2
d  # {'k1': 1, 'k2': [1], 'k3': 2}

d['k4'] = 'a'
d  # {'k1': 1, 'k2': [1], 'k3': 2, 'k4': 'a'}
```

**no built-in method for looking up key for value**

https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary

```python
x in d.values

# dict not change
d.get(key, 'not found')  # not raise error; if not found, return None
# dict changes
d.setdefault('k4', 'not found')

# don't initialize default outside
d = {'k1': 1, 'k2': [1]}
default = []
new = d.setdefault('k4', default)
print(d)
d['k4'] is default

new = d.setdefault('k5', default)
d['k4'] is d['k5']
print(d)

d['k5'].append(3)
print(d)
print(default)

d['k4'] is d['k5']  # print True

# correct version
d = {'k1': 1, 'k2': [1]}
new = d.setdefault('k4', [])
print(d)
print(d['k4'] is [])

new = d.setdefault('k5', [])
print(d['k4'] is d['k5'])
print(d)

d['k5'].append(3)
print(d)
print(default)

d['k4'] is d['k5']  # return False

# ----------------------
d = {'k1': 1, 'k2': [1]}
new = d.get('k4', [])

new2 = d.get('k5', [])

new is new2  # False

# --------------------
d = {'k1': 1, 'k2': [1]}
default = []
new = d.get('k4', default)

new2 = d.get('k5', default)

new is new2  # True
```





## Ch 15

**p. 114, `while` loop**

```python
result = 0 
idx = 0 
while idx <= len(nums): 
    if nums[idx] < 0: 
        break 
    result += nums[idx] 
    idx += 1 
                                                                                                                   
```

**`for` loops**

* Work for built-in data types of ordered sequences (str, lists, tuple, dict) and unordered collections (set).
* Note that iteration for dict loops over keys instead of values.
* Actually `for` works for any data types with `.__iter__()` defined.

```python
a = 'abc'
a = [1, 2]
a = (1, 2)
a = {1, 2}

for i in a:
    print(i, end=' ')
    
# For dict
a = {'k1': 1, 'k2': 2}
for i in a:
    print(i, end=' ')  # print k1, k2
    
print('k1' in a)  # True
```

**Tuple unpacking, multiple assignment and `enumerate()`**

* To perform multiple assignment, it is common to use tuple unpacking, although we can also unpack other data structures.
* Notat that for dict, the variables receives the content of keys.
* Multiple assignment is often used to bind variables to individual container items returned by function.
* Ref: https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/

```python
# Tuple unpacking
a = 1; b = 10
print(a, b)

a, b = 1, 10  # various forms; parenthesis doesn't matter
print(a, b)

a, b = (1, 10)
print(a, b)

(a, b) = 1, 10
print(a, b)

(a, b) = (1, 10)
print(a, b)

# For dict
a, b = {'k1': 1, 'k2': 2}
print(a,b)  # k1 k2

# Demo of enumerate():
l = ['a', 'b', 'c']

#for i, v in enumerate(l):
#for (i, v) in enumerate(l):
for [i, v] in enumerate(l):
    print(i, v)
```

**Augmented assignment**
* It works for `+`, `-`, `*`, `**`, `/`, `%`.
* Why it's more efficient than normal variable assignment: https://softwareengineering.stackexchange.com/questions/134118/why-are-shortcuts-like-x-y-considered-good-practice

```python
a = 3
a %= 2
print(a)  # 1
```

**`.index()`**

* Return the 1st index of value, if multiple items contain the value.

```python
a = [1,2,3,1]
a.index(1)  # 0

l = [1,4,5,1]
a = l[:2]
a is l  # False

a = l[:]
a is l  # False
```





## Ch 14

**Tuple unpacking**

```python
# Standard usage
# QUESTION: RHS -> tuple? LHS -> tuple?
a, b = 1, 2
print(a, b)  # 1 2

a = 1; b = 2
print(a, b)  # 1 2

# Used to unpack the tuple returned by functions
def lazy(x, y):
    return x, y

a, b = lazy(1, 2)
print(a,b)
```



**Hash, hashable, look-up in`set` and `dict`**

 * Hash is an fixed sized integer that identifies a particular value. Each value needs to have its own hash, so for the same value you will get the same hash even if it's not the same object.
 * An object is hashable if it has a hash value which never changes during its lifetime (it needs a `__hash__()` method), and can be compared to other objects (it needs an `__eq__()` method).
 * The internal structure of set and dict (the keys) requires each of its member to be hashable. This requrement makes checking membership for set and dict much faster than for list.
 * Mutable container objects (e.g. list, dict, set) are not hashable, as the value they hold change over time. Note that although each element in a set must be hashable, a set is not hashable: its state can mutate, e.g., by replacing a hashable item by another hashable one.
 * Immutable containers are only hashable if each element is hashable. A frozenset is always hashable, but a tuple is not (e.g., if it contains a list item).
 * Refs: https://stackoverflow.com/questions/17585730/what-does-hash-do-in-python, https://docs.python.org/3/glossary.html#term-hashable

```python
# A list is mutable and thus not hashable
hash([1,2])  # TypeError

# Both set types requires each member to be hashable
s = {[1], 1, 4}  # TypeError
fs = frozenset([1, 2, [1]])  # TypeError

# Two different objects can have the same hash
a = 'Look at me!'
print(hash('Look at me!') == hash(a))  # True
print(id('Look at me!') == id(a))  # False

# Hash numbers are very sensitive to values so as to prevent hash collisions
print(hash("Look at me!"))  # 5168905791375549714
print(hash("Look at me!!"))  # 3145956947722652741
```
