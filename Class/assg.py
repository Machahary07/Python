import numpy as np
py_list = [1, "Hello", 3.14]
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_result = [x + y for x, y in zip(list_a, list_b)]
np_arr = np.array([1, 2, 3]) 
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
arr_result = arr_a + arr_b
print(f"List Result: {list_result}")
print(f"NumPy Result: {arr_result}")