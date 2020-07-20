# Refractor the code such that there is a function that reads csv data from 
# any sensible iterable, which is then called by a function with file as
# iterable.

def read_csv(fname):
    with open(fname) as fin:
        return csv_to_data(fin)

def csv_to_data(iterable):
    result = []
    header = None
    for item in iterable:
        data = [val.strip() for val in item.split(',')]
        
        if header is None:
            header = data
        
        else:      
            result.append({key: data[i] for i, key in enumerate(header)})
            
    return result

fname = 'text.csv'
print(read_csv(fname))