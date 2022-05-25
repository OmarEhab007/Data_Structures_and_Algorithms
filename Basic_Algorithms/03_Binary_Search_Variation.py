# # Variations on Binary Search

# Now that you've gone through the work of building a binary search function,
# let's take some time to try out a few exercises
# that are variations (or extensions) of binary search.
# We'll provide the function for you to start:

from sympy import re


def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left  # return the index of the target
    elif source[center] < target:  # right-hand side
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:  # left-hand side
        return recursive_binary_search(target, source[:center], left)


# we wanted to find the _first_ occurrence of an element,
# rather than just any occurrence?

# Write a new function: `find_first()` that uses binary_search as a starting point.

# > Hint: You shouldn't need to modify binary_search() at all.

def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return print(index)
        if source[index-1] == target:
            index -= 1
        else:
            return print(index)

# find_first(5, [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10])
#___________________________________________________________#
# ## Contains

# The second variation is a function that returns a boolean value
# indicating whether an element is _present_,
# but with no information about the location of that element.

# Loose wrapper for recursive binary search, returning True if the index is found and False if not


def contains(target, source):
    return recursive_binary_search(target, source) is not None

# letters = ['a', 'c', 'd', 'f', 'g']
# print(contains('a', letters)) ## True
# print(contains('b', letters)) ## False

#___________________________________________________________#
# Problem statement

# Given a sorted array that may have duplicate values,
# use *binary search* to find the **first** and **last** indexes of a given value.

# For example, if you have the array `[0, 1, 2, 2, 3, 3, 3, 4, 5, 6]`
# and the given value is `3`, the answer will be `[4, 6]`
# (because the value `3` occurs first at index `4` and last at index `6` in the array).

# The expected complexity of the problem is $O(log(n))$.


def first_and_last_index(arr, number):
    # search first occurence
    first_index = find_start_index(arr, number, 0, len(arr) - 1)

    # search last occurence
    last_index = find_end_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]


def find_start_index(arr, number, start_index, end_index):
    # binary search solution to search for the first index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    # call the recursive procedure to the left-hand side of the array to find the first element
    if arr[mid_index] == number:
        current_start_pos = find_start_index(
            arr, number, start_index, mid_index - 1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos

    elif arr[mid_index] < number:  # right-hand side
        return find_start_index(arr, number, mid_index + 1, end_index)
    else:
        return find_start_index(arr, number, start_index, mid_index - 1)


def find_end_index(arr, number, start_index, end_index):
    # binary search solution to search for the last index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = mid_index
        return end_pos
    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index + 1, end_index)
    else:
        return find_end_index(arr, number, start_index, mid_index - 1)


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)
