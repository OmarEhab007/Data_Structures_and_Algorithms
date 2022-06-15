### Merge Sort ###

from Bubble_Sort import Bubble_sort
import time


def mergesort(items, call_stack=1):
    """_summary_: Merge sort algorithm

    Args:
        items (list): unsorted list of integers
        call_stack (int): numeric value of the call stack depth

    Returns:
        list: sorted list of integers
    """

    print('CALL STACK: {} \t mergesort({})'.format(call_stack, items))
    if len(items) <= 1:
        call_stack -= 1
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    print('mid index: {} \t left: {} \t   right: {}'.format(mid, left, right))

    call_stack += 1
    print('-------START: \t mergesort(left: {})'.format(left))
    left = mergesort(left, call_stack)
    print('------RETURN: \t left: {}'.format(left))
    print('---------END: \t mergesort(left: {})'.format(left))
    print('-------START: \t mergesort(right: {})'.format(right))
    right = mergesort(right, call_stack)
    print('------RETURN: \t right: {}'.format(right))
    print('---------END: \t mergesort(right: {})'.format(right))

    return merge(left, right, call_stack-1)


def merge(left, right, call_stack):

    arr = left+right
    print('MERGE CALL: \t merge({},{}) \t CALL STACK: {} \t mergesort({})'.format(
        left, right, call_stack, arr))
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('---------- list: {} --------------'.format(test_list_1))
call_stack = 1
print('RESULT : {} to {}'.format(test_list_1, mergesort(test_list_1, call_stack)))
print('---------- list: {} --------------'.format(test_list_2))
print('RESULT : {} to {}'.format(test_list_2, mergesort(test_list_2, call_stack)))
print('---------- list: {} --------------'.format(test_list_3))
print('RESULT : {} to {}'.format(test_list_3, mergesort(test_list_3, call_stack)))
