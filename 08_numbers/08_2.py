def check_divisible(num1, num2):
    assert num2, 'Divisor is zero!'

    remainder = num1 % num2
    
    if remainder:
        print(f'{num1} is not divisible by {num2}')
    else:
        print(f'{num1} is divisible by {num2}')


check_divisible(297, 3)
check_divisible(297, 0)