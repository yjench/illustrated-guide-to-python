# Can further reduce search space using the fact that except 2, all primes 
# are odd numbers: https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
from math import ceil, sqrt

# Method 1: standard for loop
def is_prime(num):
    prime = True
    
    for i in range(2, ceil(sqrt(num))):
        if not num % 2:
            prime = False
            break
    
    return num > 1 and prime

for num in [2, 3, 5, 12, 25]:
    print(f'{num} -> {is_prime(num)}')
    
print('-' * 12)

# Method 2: use all (less efficient than for loop for non-prime)
def is_prime(num):
    return num > 1 and all([num % i for i in range(2, ceil(sqrt(num)))])

for num in [2, 3, 5, 12, 25]:
    print(f'{num} -> {is_prime(num)}')