import pytest
from merge.merge import MergeSort

def test_reverse_sorted():
    arr = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    merge_sort = MergeSort()
    merge_sort.sort(arr)
    assert arr == expected

def test_few_uniques():
    arr = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    merge_sort = MergeSort()
    merge_sort.sort(arr)
    assert arr == expected

def test_nearly_sorted():
    arr = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    merge_sort = MergeSort()
    merge_sort.sort(arr)
    assert arr == expected
