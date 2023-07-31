import pytest
from hashmap_left_join.hashmap_left_join import left_join

def test_left_join_equal_tables():
    hashTable1 = {'a': 1, 'b': 2, 'c': 3}
    hashTable2 = {'a': 10, 'b': 20, 'c': 30}
    actual_output = left_join(hashTable1, hashTable2)
    expected_output = [['a', 1, 10], ['b', 2, 20], ['c', 3, 30]]
    assert actual_output == expected_output

def test_left_join_missing_values():
    hashTable1 = {'a': 1, 'b': 2, 'c': 3}
    hashTable2 = {'a': 10, 'c': 30}
    actual_output = left_join(hashTable1, hashTable2)
    expected_output = [['a', 1, 10], ['b', 2, None], ['c', 3, 30]]
    assert actual_output == expected_output

def test_left_join_empty_table2():
    hashTable1 = {'a': 1, 'b': 2, 'c': 3}
    hashTable2 = {}
    actual_output = left_join(hashTable1, hashTable2)
    expected_output = [['a', 1, None], ['b', 2, None], ['c', 3, None]]
    assert actual_output == expected_output