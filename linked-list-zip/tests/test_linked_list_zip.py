import pytest
from linked_list_zip.linked_list_zip import LinkedList, zipLists

def test_zipLists_equal_length():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    result = zipLists(list1, list2)
    expected = [1, 2, 3, 4, 5, 6]
    assert result.to_list() == expected, f"Expected: {expected}, Actual: {result.to_list()}"

def test_zipLists_different_lengths():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)

    result = zipLists(list1, list2)
    expected = [1, 2, 3, 4, 5]
    assert result.to_list() == expected, f"Expected: {expected}, Actual: {result.to_list()}"

def test_zipLists_one_empty_list():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()

    result = zipLists(list1, list2)
    expected = [1, 3, 5]
    assert result.to_list() == expected, f"Expected: {expected}, Actual: {result.to_list()}"

def test_zipLists_both_empty_lists():
    list1 = LinkedList()
    list2 = LinkedList()

    result = zipLists(list1, list2)
    expected = []
    assert result.to_list() == expected, f"Expected: {expected}, Actual: {result.to_list()}"

def test_zipLists_different_types():
    list1 = LinkedList()
    list1.append("apple")
    list1.append("banana")

    list2 = LinkedList()
    list2.append(1)
    list2.append(2)

    result = zipLists(list1, list2)
    expected = ["apple", 1, "banana", 2]
    assert result.to_list() == expected, f"Expected: {expected}, Actual: {result.to_list()}"