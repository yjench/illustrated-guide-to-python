# Method 0: Benchmark solution
from calendar import isleap

# Method 1: Flattened conditionals
def isleap_1(y):
    if y % 400 == 0:
        leap = True
    elif y % 100 == 0:
        leap = False
    elif y % 4 == 0:
        leap = True
    else:
        leap = False
    return leap
        
# Method 2: Conditionals with proper initialization and boolean operations
def isleap_2(y):
    leap = False
    if y % 400 == 0:
        leap = True
    elif y % 4 == 0 and y % 100 != 0:
        leap = True
    return leap
        
# Method 3: One liner using compound booleans and short circuit
def isleap_3(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


for y in [1800, 1900, 1903, 2000, 2002]:
    ans = [isleap(y), isleap_1(y), isleap_2(y), isleap_3(y)]
    assert all([ans[i] is ans[0] for i in range(1, 4)])
    print(f'{y} is leap year? {ans[0]}')