"""
A module for converting temperatures between Fahrenheit and Celsius.
"""

def fahrenheit_celsius_conv(temp, unit="F"):
    """
    Convert a temperature between Fahrenheit and Celsius.

    Parameters
    ----------
    temp : float
        The temperature to be converted.
    unit : str, optional
        The unit of the input temperature. Use "F" to convert Fahrenheit to
        Celsius, or "C" to convert Celsius to Fahrenheit. Default is "F".

    Returns
    -------
    float
        The converted temperature.

    Examples
    --------
    >>> fahrenheit_celsius_conv(32, unit="F")
    0.0
    >>> fahrenheit_celsius_conv(0, unit="C")
    32.0
    """
    if unit == "F":
        return (temp - 32) * 5 / 9
    else:
        return (temp * 9 / 5) + 32