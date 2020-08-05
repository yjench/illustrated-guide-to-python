names = ['John', 'Tommy', 'Fredrich', 'Jan']

# Method 1: standard for loop
tot_chars = 0
for name in names:
    tot_chars += len(name)

print(f'Averaged length of names: {tot_chars / len(names)}')
print('-'*30)

# Method 2: map
tot_chars = sum(map(len, names))

print(f'Averaged length of names: {tot_chars / len(names)}')