
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
