def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "yes"
    else:
        return "no"
def leap_years_in_century(century):
    start_year = (century - 1) * 100
    end_year = century * 100
    for year in range(start_year, end_year):
        if is_leap_year(year) == "yes":
            print(year)