for y in [1800, 1900, 1903, 2000, 2002]:
        
    # Benchmark solution
    from calendar import isleap
    leap = isleap(y)
    print(f'Method 0: {y} is leap year? {leap}')
    
    # Flatten conditionals by exploiting order of conditionals
    if y % 400 == 0:
        leap = True
    elif y % 100 == 0:
        leap = False
    elif y % 4 == 0:
        leap = True
    else:
        leap = False
    print(f'Method 1: {y} is leap year? {leap}')
    
    # Flatten conditionals by proper initialization and compound booleans
    leap = False
    if y % 400 == 0:
        leap = True
    elif y % 4 == 0 and y % 100 != 0:
        leap = True
    print(f'Method 2: {y} is leap year? {leap}')
    
    # One liner using conditional expression and short circuit
    leap = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    print(f'Method 3: {y} is leap year? {leap}')
    
    print('\n')