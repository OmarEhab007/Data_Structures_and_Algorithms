### Bubble Sort ###
import time

wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22,
                13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]


def Bubble_sort(list):
    """_summary_: Bubble sort algorithm

    Args:
        list (int): unsorted list of integers

    Returns:
        list: sorted list of integers
    """
    for iterations in range(len(list)):
        for index in range(1, len(list)):
            if list[index-1] > list[index]:
                list[index-1], list[index] = list[index], list[index-1]
    return list
