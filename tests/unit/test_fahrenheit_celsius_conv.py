"""
A test module that tests the temp_conv module.
"""

from unitconv.temp_conv import fahrenheit_celsius_conv

def test_fahrenheit_celsius_conv():
    """
    Test that fahrenheit_celsius_conv works as expected
    """
    # Test F to C: freezing point
    assert fahrenheit_celsius_conv(32, unit="F") == 0.0, "32F should be 0C"

    # Test F to C: boiling point
    assert fahrenheit_celsius_conv(212, unit="F") == 100.0, "212F should be 100C"

    # Test C to F: freezing point
    assert fahrenheit_celsius_conv(0, unit="C") == 32.0, "0C should be 32F"

    # Test C to F: boiling point
    assert fahrenheit_celsius_conv(100, unit="C") == 212.0, "100C should be 212F"