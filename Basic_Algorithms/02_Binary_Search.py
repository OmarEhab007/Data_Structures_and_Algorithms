# # Binary search practice

# Let's get some practice doing binary search on an array of integers.
# We'll solve the problem two different ways—both iteratively and resursively.

# Here is a reminder of how the algorithm works:

# 1. Find the center of the list (try setting an upper and lower bound to find the center)
# 2. Check to see if the element at the center is your target.
# 3. If it is, return the index.
# 4. If not, is the target greater or less than that element?
# 5. If greater, move the lower bound to just above the current center
# 6. If less, move the upper bound to just below the current center
# 7. Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).


# ## Problem statement:
# Given a sorted array of integers, and a target value,
# find the index of the target value in the array.
# If the target value is not present in the array, return -1.

# ## Iterative solution

# First, see if you can code an iterative solution (i.e., one that uses loops). If you get stuck, the solution is below.


def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    lower = 0
    upper = len(array) - 1

    for i in range(len(array)):
        center = (lower + upper) // 2
        if array[center] == target:
            return center
        elif target < array[center]:
            upper = center - 1
        else:
            lower = center + 1
    return print("this number is not in the array")

# binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)


def binary_search_recursive(array, target, lower=0, upper=None):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if len(array) == 0:
        return print("this number is not in the array")
    if upper is None:
        upper = len(array) - 1

    center = (lower + upper) // 2
    if array[center] == target:
        return center
    elif target < array[center]:
        return binary_search_recursive(array, target, lower, center - 1)
    elif target > array[center]:
        return binary_search_recursive(array, target, center + 1, upper)

# binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
