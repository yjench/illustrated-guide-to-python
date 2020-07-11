def check_leap_year(year):
    if year % 400 == 0:
        print(f'{year}: leap year')
    elif year % 100 == 0:
        print(f'{year}: not leap year')
    elif year % 4 == 0:
        print(f'{year}: leap year')
    else:
        print(f'{year}: not leap year')


years = [1800, 1900, 1903, 2000, 2002]

for year in years:
    check_leap_year(year)