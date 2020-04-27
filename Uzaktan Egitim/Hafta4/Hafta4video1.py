# -*- coding: utf-8 -*-
"""

Heapsort

@author: Elif
"""

def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array


my_array_2=heapsort(my_array_1)
print(my_array_1, my_array_2)