
import numpy as np

def change_array():

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # reshape(arrays, elements)
    # The outermost dimension will have 4 arrays, each with 3 elements
    newarr = arr.reshape(4, 3)
    return newarr


print(change_array())