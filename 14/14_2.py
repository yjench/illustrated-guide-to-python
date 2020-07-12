import operator

people = []

me = ('Yiyi', 'Chen', 10)
people.append(me)

yaya = ('Yaya', 'Laplace', 15)
people.append(yaya)

print(f'Sorted list (default): {sorted(people)}')
print(f'Sorted list (item 0): {sorted(people, key=operator.itemgetter(0))}')
print(f'Sorted list (item 1): {sorted(people, key=operator.itemgetter(1))}')
print(f'Sorted list (item 2): {sorted(people, key=operator.itemgetter(1))}')