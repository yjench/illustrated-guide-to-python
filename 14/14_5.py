list_attributes = set(dir([]))
tuple_attributes = set(dir(()))

unique_list_attributes = list_attributes - tuple_attributes
print(unique_list_attributes)