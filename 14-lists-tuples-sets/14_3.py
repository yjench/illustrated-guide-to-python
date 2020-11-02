names = ['Yi-Jen', 'John', 'Franny', 'Franny']
top_names = ['John', 'Mary', 'Ted']

print(f'Friends\' names that are common names: ')
print(f'{set(names) & set(top_names)}')