import pytest

from Linked_List.Linked_List import (Node , linked_list)

def test_empty_linked_list():
    test = linked_list()
    actual = test.head
    expected = None
    assert actual == expected

def test_insert_into_the_linked_list():
     test2 = linked_list()
     test2.insert("mahdi")
     actual = test2.head.value  
     expected = "mahdi"
     assert actual == expected


def test_point_to_the_first_node():
     node_l = Node("Hi")
     node_M = Node("Mahdi", node_l)
     ll_ = linked_list(node_M)
     actual = ll_.head.value
     expected = "Mahdi"
     assert actual == expected

def test_insert_multiple_into_the_linked_list():
    node_l = Node("Hi")
    node_M = Node("Mahdi", node_l)
    actual = node_M.value
    expected = "Mahdi"
    assert actual == expected


def test_linked_listlinked_that_exists():
     node_l = Node("Hi")
     node_M = Node("Mahdi", node_l)
     ll_ = linked_list(node_M)
     check = ll_.includes("Hi")
     actual = check
     expected = True
     assert actual == expected


def test_linked_listlinked_that_not_exists():
     node_l = Node("Hi")
     node_M = Node("Mahdi", node_l)
     ll_ = linked_list(node_M)
     check = ll_.includes("Hello")
     actual = check
     expected = False
     assert actual == expected
    

def test_linked_list_values():
     node_l = Node("Hi")
     node_M = Node("Mahdi", node_l)
     ll_ = linked_list(node_M)
     output =ll_.to_string ()

     actual = output
     expected = "{ Mahdi }-> { Hi }->  None "
     assert actual == expected

def test_append_to_the_linked_list():
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(2)
    node1.next = node2
    node2.next = node3

    my_list = linked_list(node1)
    my_list.append(5)
    actual = my_list.to_string()
    expected = "{ 1 }-> { 3 }-> { 2 }-> { 5 }->  None "
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"

def test_insert_before_in_linked_list():
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(2)

    node1.next = node2
    node2.next = node3
    my_list = linked_list(node1)
    my_list.insert_before(3, 5)
    actual = my_list.to_string()
    expected = "{ 1 }-> { 5 }-> { 3 }-> { 2 }->  None "
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"

def test_insert_after_in_linked_list():
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(2)
    node1.next = node2
    node2.next = node3
    my_list = linked_list(node1)
    my_list.insert_after(3, 5)
    actual = my_list.to_string()
    expected = "{ 1 }-> { 3 }-> { 5 }-> { 2 }->  None "
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"




    
    
    

