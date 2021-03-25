def check_leap_year(year):
    leap = False
    if not year % 400:
        leap = True
    elif not year % 4 and year % 100:
        leap = True
    
    print(f'{year} is leap year' if leap else f'{year} is not leap year')


years = [1800, 1900, 1903, 2000, 2002]
for year in years:
    check_leap_year(year)