def check_leap_year(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
       
    print(f'{year} is leap year' if leap else f'{year} is not leap year')


years = [1800, 1900, 1903, 2000, 2002]

for year in years:
    check_leap_year(year)