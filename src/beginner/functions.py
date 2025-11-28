# functions are used for reusability

# list of days in a month
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# validate year whether  leap
def is_leap_year(year: int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# get days in a month of the given year
def get_days(year: int, month: int):
    if not 1 <= month <= 12:
        raise ValueError("Invalid month! it should be between 1 and 12")

    return 29 if is_leap_year(year) and month == 2 else days[month]


if __name__ == "__main__":
    month_days = get_days(2000, 2)
    print(f"days: {month_days}")
