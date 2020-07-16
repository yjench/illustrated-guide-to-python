def is_odd(num: int) -> bool:
    return bool(num % 2)

for num in range(-2, 2):
    print(f'{num} is odd? {is_odd(num)}')