# Problem Statement
# You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.
#
# Example 1:
#
# arr= [1, 2, 3, -4, 6]
# The largest sum is 8, which is the sum of all elements of the array.
# Example 2:
#
# arr = [1, 2, -5, -4, 1, 6]
#

def max_sum_subarray(arr):
   """get the max sum of a subarray

   Args:
      arr (list): list of number to find the max sum of a subarray

   Returns:
      int: max sum of a subarray
   """
   current_sum = arr[0]
   max_sum = arr[0]
   for num in arr[1:]:
      current_sum = max(current_sum+num, num)
      max_sum = max(current_sum, max_sum)
   return max_sum


def test_function(test_case):
   arr = test_case[0]
   solution = test_case[1]

   output = max_sum_subarray(arr)
   if output == solution:
      print("Pass")
   else:
      print("Fail")


arr = [1, 2, 3, -4, 6]
solution = 8  # sum of array

test_case = [arr, solution]
test_function(test_case)
