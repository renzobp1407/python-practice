from typing import Union

def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError("the divisor cannot be zero.")
    
    return dividend / divisor

