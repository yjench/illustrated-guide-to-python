names = []
print(f'ID of empty list: {id(names)}')

names.append('John')
names.append('Carol')
names.append('Tommy')
print(f'ID of populated list: {id(names)}')

names.sort()
print(f'Sorted list: {names}')