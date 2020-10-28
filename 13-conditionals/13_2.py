# Method 1: conditional expression
def is_odd_1(num):
    return True if num % 2 else False
 
# Method 2: bool constructor
def is_odd_2(num):
    return bool(num % 2)
    

for num in range(-2, 3, 2):
    assert is_odd_1(num) is is_odd_2(num)
    print(f'{num} is odd?', is_odd_1(num))