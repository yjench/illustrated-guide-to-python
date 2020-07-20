# Refactor the function such that there is a function that writes csv data to 
# any sensible iterable, which is then called by a function with file as
# iterable.

def write_csv(fname, data):
    with open(fname, 'w') as fout:
        lines = data_to_csv(data)
        for line in lines:
            fout.write(line + '\n')

def data_to_csv(data):
    result = []
    header = 'name, address, age'
    result.append(header)
    for item in data:
        result.append('{}, {}, {}'.format(*item))
        
    return result

fname = 'text.csv'
data = [('George', '4312 Abbey Road', 22),
        ('John', '54 Love Ave', 21)]
write_csv(fname, data)