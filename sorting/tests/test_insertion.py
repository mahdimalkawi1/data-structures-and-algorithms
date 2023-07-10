import pytest
from insertion.insertion import InsertionSort

def test_insertion_sort():
    insertion_sort = InsertionSort([])
    assert insertion_sort.sort() == []

    insertion_sort = InsertionSort([1])
    assert insertion_sort.sort() == [1]

    input_list = [4, 2, 7, 1, 5]
    expected_output = [1, 2, 4, 5, 7]
    insertion_sort = InsertionSort(input_list)
    assert insertion_sort.sort() == expected_output

    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected_output = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    insertion_sort = InsertionSort(input_list)
    assert insertion_sort.sort() == expected_output

    input_list = [-5, -2, 0, -8, -1]
    expected_output = [-8, -5, -2, -1, 0]
    insertion_sort = InsertionSort(input_list)
    assert insertion_sort.sort() == expected_output
