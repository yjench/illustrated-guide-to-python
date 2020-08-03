for y in [1800, 1900, 1903, 2000, 2002]:
    ans = []    
    
    # Method 0: Benchmark solution
    from calendar import isleap
    leap = isleap(y)
    ans.append(leap)
    
    # Method 1: Flatten conditionals by exploiting order of conditionals
    if y % 400 == 0:
        leap = True
    elif y % 100 == 0:
        leap = False
    elif y % 4 == 0:
        leap = True
    else:
        leap = False
    ans.append(leap)
    
    # Method 2: Flatten conditionals by proper initialization & compound booleans
    leap = False
    if y % 400 == 0:
        leap = True
    elif y % 4 == 0 and y % 100 != 0:
        leap = True
    ans.append(leap)
    
    # Method 3: One liner using conditional expression and short circuit
    leap = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    ans.append(leap)
    
    # Tests
    assert all([ans[i] == ans[0] for i in range(1, 4)])
    print(f'{y} is leap year? {ans[0]}')