from typing import Union

def divide(dividend: Union[int, float], divisor: Union[int, float]):
    return dividend / divisor

def multiply(*args: tuple[Union[int, float]]):
    if len(args) == 0:
        raise ValueError('at least one value to multiply must be passed.')
    total = 1
    for arg in args:
        total *=arg

    return total    
