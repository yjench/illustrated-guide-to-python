names = ['Tommy', 'Fredrich', 'Jan', 'Donald']
query = 'John'

# Method 1: for loop
for name in names:
    if name == query:
        print('Target name found')
        break
else:
    print('Target name not found')

print('-'*30)

# Method 2: use `in`
msg = 'Target name found' if query in names else 'Target name not found'
print(msg)