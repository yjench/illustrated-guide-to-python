# Note that a string of length 0 or 1 is always a palindrome

# Method 1: slicing
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Method 2: while loop
def is_palindrome_iter(s):
    s = s.lower()
    
    is_pal = True
    while s:
        if s[0] != s[-1]:
            is_pal = False
            break
        
        s = s[1:-1]
        
    return is_pal

# Method 3: recursion
def is_palindrome_recur(s):
    s = s.lower()
    if not s:
        return True
    
    else:
        return s[0] == s[-1] and is_palindrome_recur(s[1:-1])

# Tests
for s in ('', 'a', 'aba', 'hdksdh'):
    ans = [is_palindrome(s), is_palindrome_iter(s), is_palindrome_recur(s)]
    assert all([ans[i] == ans[j] for i in range(3) for j in range(3) if j > i])
    print(f'String {s} is palindrome: ', *ans)