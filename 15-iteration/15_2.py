names = ['Tommy', 'Fredrich', 'Jan', 'Donald']
target = 'John'

# Method 1: for loop
for name in names:
    if name == target:
        print('Target name found')
        break
else:
    print('Target name not found')
print('-'*30)

# Method 2: use `in`
msg = 'Target name found' if target in names else 'Target name not found'
print(msg)