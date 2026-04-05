# Welcome to unitconv-dsci310

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/unitconv.svg)](https://pypi.org/project/unitconv-dsci310/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/unitconv-dsci310.svg)](https://pypi.org/project/unitconv-dsci310/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

unitconv-dsci310 is a lightweight Python package for converting between common units of measurement. Currently it supports temperature conversions between Fahrenheit and Celsius.

## Get started

You can install this package into your preferred Python environment using pip:

```{bash}
$ pip install unitconv-dsci310
```

## Usage

To convert a temperature from Fahrenheit to Celsius:

```{python}
from unitconv import fahrenheit_celsius_conv

# Convert 32°F to Celsius
fahrenheit_celsius_conv(32, unit="F")  # returns 0.0

# Convert 100°C to Fahrenheit
fahrenheit_celsius_conv(100, unit="C")  # returns 212.0
```

The `unit` parameter specifies the unit of the **input** temperature:

- `"F"` — converts Fahrenheit to Celsius (default)
- `"C"` — converts Celsius to Fahrenheit

## Copyright

- Copyright © 2026 Shivani Aggarwal.
- Free software distributed under the [MIT License](./LICENSE).
