# shortint Module

This is a simple, lightweight Python module to let you abbreviate numbers in their longer versions and extend numbers from their shortened versions.

This project was inspired by [millify](https://github.com/azaitsev/millify) by Alex Zaitsev that would convert long numbers into a more readable format. I was heavily intrigued by the idea, but realised I needed the reverse and that my searches online were to no avail. I also included a feature Alex had, which was allowing for custom units in his conversions.

## Installation

There are two ways to download this project:

1. From PyPI:
```
pip install shortint
```

2. From GitHub:
```
pip install git+https://github.com/axololly/shortint
```

## Usage

There are two functions that come included:

1. `shortint.shortint()`
```py
>>> import shortint
>>> shortint.shortint(123_000)
'123k'
>>> shortint.shortint(923_324, precision = 2)
'923.32k'
```

2. `shortint.longint()`
```py
>>> import shortint
>>> shortint.longint('456k')
456000 # 456,000
>>> shortint.longint('14.325m')
14325000 # 14,325,000
```