# Notes:
# - The order of lower and upper bounds would be flipped for empty sequence
#   or if target is not in sequence
#
# - As int in Pythin can be arbitrarily long, there is no problem of index 
#   overflow: https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html

# Method 1: iteration
def bisec_iter(x, seq):  
    low, high = 0, len(seq) - 1
    
    while low <= high:
        idx = (low + high) // 2
        
        if seq[idx] == x:
            return idx
        
        elif seq[idx] < x:
            low = idx + 1
            
        else:
            high = idx -1
            
    return -1

# Method 2: recursion
def bisec_recur(x, seq):
    
    def recur(low, high):
        idx = (low + high) // 2
        
        # Base cases
        if low > high:
            return -1
    
        elif seq[idx] == x:
            return idx

        # Recursive cases
        elif seq[idx] < x:
            return recur(idx+1, high)
    
        else:
            return recur(low, idx-1)
    
    return recur(0, len(seq)-1)

# Tests
for x, seq in ((3, range(0)), (1, range(5)), (8, range(6)),
               ('a', ''), ('m', 'ambd'), ('k', 'sadiops')):
    print(f'Target {x} in sequence {seq}:')
    print(f'Index (iter, recur): {bisec_iter(x, seq)}, {bisec_recur(x, seq)}')
    print()