"Module for expanding shortened versions of numbers to their normal long counterparts."

from math import log10

def longint(value: str) -> int:
    """
    ### Explanation:
    Turn an abbreviated number in the format `"...U"` into its normal long form.

    This only works using the following standard units:
        - `k` - 1,000
        - `m` - 1,000,000
        - `b` - 1,000,000,000
        - `t` - 1,000,000,000,000

    ### Parameters:
        - value: `str` - the abbreviated number to convert to its full self.

    ### Returns:
        - `int` - the integer the abbreviated version was representing.

    ### Raises:
        - `ValueError` - `value` argument was not a `str`.
        - `InterruptedError` - unit was invalid.
        - `ArithmeticError` - number was not a valid number. (eg. like "123.14.179.18")

    ### Examples:
    >>> from shortint import longint
    >>> longint('123k')
    123000
    >>> longint('1.249m')
    1249000
    """

    if not isinstance(value, str):
        raise ValueError('value argument must be a string.')
    
    *N, U = value
    N = ''.join(N)
    U = U.lower()

    exps = {'k': 3, 'm': 6, 'b': 9, 't': 12}

    if U not in exps.keys():
        raise InterruptedError('unit is not valid. Check docstring for valid units.')
    
    try:
        N = float(N)
    except ValueError:
        raise ArithmeticError('number is not a valid number.')

    val: float = N * 10 ** exps[U]

    if val.is_integer():
        return int(val)
    
    return val