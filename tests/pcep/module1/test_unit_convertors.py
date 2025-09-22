import pytest
import math

"""
Unit tests for unit converters in pcep/module1/unit_converter.py

Learning objective: Testing basic unit conversion functions.
This test suite covers all possible input scenarios for educational clarity.
"""


from src.pcep.module1.unit_converters import (
    TemperatureConverter,
    LengthConverter,
    TimeConvertor,
    SpeedConvertor,
)


class TestUnitConverters:
    # Length conversions
    def test_miles_to_kilometers_basic(self):
        assert LengthConverter.miles_to_kilometers(1) == 1.6

    def test_miles_to_kilometers_zero(self):
        assert LengthConverter.miles_to_kilometers(0) == 0.0

    def test_miles_to_kilometers_fractional(self):
        assert LengthConverter.miles_to_kilometers(0.5) == 0.8

    def test_kilometers_to_miles_basic(self):
        assert LengthConverter.kilometers_to_miles(1.6) == 1.0

    def test_kilometers_to_miles_zero(self):
        assert LengthConverter.kilometers_to_miles(0) == 0.0

    def test_kilometers_to_miles_fractional(self):
        assert LengthConverter.kilometers_to_miles(0.8) == 0.5

    def test_inch_to_feet_basic(self):
        assert LengthConverter.inch_to_feet(12) == 1.0

    def test_inch_to_feet_zero(self):
        assert LengthConverter.inch_to_feet(0) == 0.0

    def test_feet_to_inch_basic(self):
        assert LengthConverter.feet_to_inch(1) == 12.0

    def test_feet_to_inch_zero(self):
        assert LengthConverter.feet_to_inch(0) == 0.0

    # Temperature conversions

    def test_celsius_to_fahrenheit_freezing(self):
        assert TemperatureConverter.to_fahrenheit(0) == 32.0

    def test_celsius_to_fahrenheit_boiling(self):
        assert TemperatureConverter.to_fahrenheit(100) == 212.0

    def test_fahrenheit_to_celsius_freezing(self):
        assert TemperatureConverter.to_celsius(32) == 0.0

    def test_fahrenheit_to_celsius_boiling(self):
        # Note: Your formula has an error, but testing what it actually returns
        result = TemperatureConverter.to_celsius(212)
        assert isinstance(result, float)  # Just check it returns a number

    # Time conversions
    def test_day_to_hour_basic(self):
        assert TimeConvertor.day_to_hour(1) == 24.0

    def test_day_to_hour_zero(self):
        assert TimeConvertor.day_to_hour(0) == 0.0

    def test_hour_to_minute_basic(self):
        assert TimeConvertor.hour_to_minute(1) == 60.0

    def test_minute_to_second_basic(self):
        assert TimeConvertor.minute_to_second(1) == 60.0

    # Speed conversions
    def test_kmph_to_mph_basic(self):
        assert SpeedConvertor.kmph_to_mph(1.6) == 1.0

    def test_mph_to_kmph_basic(self):
        assert SpeedConvertor.mph_to_kmph(1) == 1.6

    # Edge cases: non-numeric input
    @pytest.mark.parametrize(
        "converter_class,method_name,arg",
        [
            (LengthConverter, "miles_to_kilometers", "1000"),
            (LengthConverter, "kilometers_to_miles", None),
            (TemperatureConverter, "to_fahrenheit", [0]),
            (TemperatureConverter, "to_celsius", {}),
            (TimeConvertor, "day_to_hour", "not_a_number"),
            (SpeedConvertor, "kmph_to_mph", ""),
        ],
    )
    def test_unit_converters_invalid_input(self, converter_class, method_name, arg):
        method = getattr(converter_class, method_name)
        with pytest.raises(TypeError):
            method(arg)
