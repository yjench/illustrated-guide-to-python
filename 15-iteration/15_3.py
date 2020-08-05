people = [('Donald', 'Trump', 74),
          ('John', 'Harrison', 35),
          ('Yiyi', 'Chen', None)]

def check_age(avg_age, people):
    for first_name, last_name, age in people:
        if age is None:
            print(f'{first_name}: age unknown... likely old')
        elif age >= avg_age:
            print(f'{first_name} is old')
        else:
            print(f'{first_name} is young')   

# Method 1: standard for loop
ages = []
for first_name, last_name, age in people:
    if age is not None:
        ages.append(age)
        
avg_age = sum(ages) / len(ages)
check_age(avg_age, people)

print('-'*30)  
        
# Method 2: list comprehension
ages = [person[2] for person in people if person[2] is not None]
avg_age = sum(ages) / len(ages)

check_age(avg_age, people)