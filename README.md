# `humanint` Module

This is a simple, lightweight Python module to let you abbreviate numbers in their longer versions and extend numbers from their shortened versions.

This project was inspired by [millify](https://github.com/azaitsev/millify) by Alex Zaitsev that would convert long numbers into a more readable format. I was heavily intrigued by the idea, but realised I needed the reverse and that my searches online were to no avail. I also included a feature Alex had, which was allowing for custom units in his conversions.

Thank you to Soheab for the improved naming scheme.

## Installation

From GitHub:
```
pip install git+https://github.com/axololly/humanint
```

## Usage

There are two functions that come included:

1. `humanint.to_human()`
    - Abbreviate a number into a human-readable format.
    - Includes a `precision` kwarg for abbreviated results including decimals.
    - Optional `units` argument to replace standard units with units of your choice.
```py
>>> import humanint
>>> humanint.to_human(123_000)
'123k'
>>> humanint.to_human(923_324, precision = 2)
'923.32k'
```

2. `humanint.from_human()`
    - Turn an abbreviated number back into its normal form.
    - No support for custom units.
```py
>>> import humanint
>>> humanint.from_human('456k')
456000 # 456,000
>>> humanint.from_human('14.325m')
14325000 # 14,325,000
```

## Improvements

I'm always open to improvements. Give me your best suggestions, and thank you for viewing my project :)