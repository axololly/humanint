from math import log10
from typing import Union

def _round(value: float, precision: int) -> Union[int, float]:
    """
    ### Explanation:
    Round a decimal number (a float) to a given precision.

    ### Parameters:
        - value: `float` - the value to round.
        - precision: `int` - how many decimal places to round to.

    ### Returns:
        - `Union[int, float]` - the rounded number, converted to an `int` if possible.

    ### Examples:
    >>> _round(145.569, 2)
    145.57
    >>> _round(356.6, 0)
    357
    >>> _round(184.14, 3) # no third decimal to round
    184.14
    """

    if isinstance(value, int):
        return value # no decimal places
    
    if not isinstance(value, float):
        raise ValueError('value argument must be a float.')
    
    if not isinstance(precision, int):
        raise ValueError('precision argument must be an integer.')
    
    if precision < 0:
        raise ArithmeticError('precision argument must be a non-zero integer.')

    n = float(f'%.{precision}f' % value)
    
    if n.is_integer():
        return int(n)
    
    return n