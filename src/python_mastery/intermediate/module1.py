# importing module in python
# lets explore some basic standard libraries
import datetime

# let's explore some commonly used standard library modules
import math

# time module has been imported
# importing specific name from module
from datetime import datetime

# importing specific entity from module with alias
from datetime import datetime as dt

# importing from other package
from ..beginner import module1

# importing entity from the current package itslef
from .my_module1 import MyClass1

# importing entity from sub_package from the current package
from .sub_package.test import MyClass4, MyClass5, MyClass6


class MathUtil:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def abs(number: int | float):
        return abs(number)

    @staticmethod
    def area_circle(radius: int | float):
        return math.pi * (radius**2)


class DateTimeUtil:
    @staticmethod
    def current_time():
        return dt.now().strftime("%H:%M:%S")

    @staticmethod
    def current_date():
        return dt.now().strftime("%Y-%m-%d")

    @staticmethod
    def total_days(start_date: dt, end_date: dt):
        return (end_date - start_date).days

    @staticmethod
    def total_minutes(start_dt: dt, end_dt: dt):
        return (end_dt - start_dt).total_seconds() / 60


if __name__ == "__main__":
    # print("Waitng for 10 Seconds...")
    # for i in range(1, 11):
    #     time.sleep(1)
    #     print(i)
    now = datetime.now()
    print(now)  # prints the current time

    now = dt.now()
    print(now)

    # testing math utils
    print(MathUtil.add(1, 2, 3))
    print(MathUtil.abs(10))
    print(MathUtil.abs(-10))
    print(MathUtil.abs(-1.0))
    print(MathUtil.area_circle(5))
    print(MathUtil.area_circle(6.3))

    # importing custom module
MyClass1.my_print("I am getting printed from custom printer")
