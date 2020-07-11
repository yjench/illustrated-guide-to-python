def check_object(obj):
    print('Contents of object')
    print('------------------')
    print('ID:', id(obj))
    print('Type:', type(obj))
    print('Value:', obj, '\n')

l = []
check_object(l)

l.append(300)
check_object(l)
