def is_odd(num):
    return bool(num % 2)  # or: return True if num % 2 else False

for num in range(-2, 3):
    print(f'{num} is odd?', is_odd(num))