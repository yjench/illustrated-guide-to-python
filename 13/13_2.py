for num in range(2):
    print(f'{num} is odd?', end=' ')

    ans1 = True if num % 2 else False  # use truthy/falsey
    ans2 = bool(num % 2) or False  # use short-circuit evaluation
    print(ans1, ans2)