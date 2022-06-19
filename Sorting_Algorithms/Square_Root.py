"""Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
    """


def sqrt(number : int) -> int:
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    # Handel null input
    if number is None:
        return None
    
    #handel negative input
    if number < 0:
        raise ValueError("Number must be positive")
    
    #handel base cases
    if (number == 0 or number == 1):
        return number
    
    #do Binary search for floor(sqrt(number))
    lower_bound = 0
    upper_bound = number // 2
    
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        middle_square = middle * middle
        if middle_square == number:
            return middle
        
        if middle_square < number:
            lower_bound = middle + 1
            guess = middle
        else:
            upper_bound = middle -1
    
    return guess


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
