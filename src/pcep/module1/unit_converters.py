class TypeValidator:
    def __init__(self, func):
        self.func = func

    def __call__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"{self.func.__name__} operates only on int and float only!"
            )
        return self.func(value)


class TemperatureConverter:

    @staticmethod
    @TypeValidator
    def to_fahrenheit(celsius):
        return round((celsius * 9 / 5) + 32, 1)

    @staticmethod
    @TypeValidator
    def to_celsius(fahrenheit):
        return round((fahrenheit - 32) * 5 / 9, 1)


class LengthConverter:

    @staticmethod
    @TypeValidator
    def miles_to_kilometers(miles):
        return round(miles * 1.6, 2)

    @staticmethod
    @TypeValidator
    def kilometers_to_miles(kilometers):
        return round(kilometers / 1.6, 2)

    @staticmethod
    @TypeValidator
    def inch_to_feet(inch):
        return round(inch / 12, 2)

    @staticmethod
    @TypeValidator
    def feet_to_inch(feet):
        return round(feet * 12, 2)


class TimeConvertor:

    @staticmethod
    @TypeValidator
    def day_to_hour(day):
        return round(day * 24, 2)

    @staticmethod
    @TypeValidator
    def hour_to_minute(hour):
        return round(hour * 60, 2)

    @staticmethod
    @TypeValidator
    def minute_to_second(minute):
        return round(minute * 60, 2)


class SpeedConvertor:

    @staticmethod
    @TypeValidator
    def kmph_to_mph(kmph):
        return round(kmph / 1.6, 2)

    @staticmethod
    @TypeValidator
    def mph_to_kmph(mph):
        return round(mph * 1.6, 2)
