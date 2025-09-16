def leap_year(year: int) -> bool:
    """
    determines whether a given year is a leap year
    """
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0
