import pytest
from stack_and_queue.queue import Queue  # Import Queue class from the appropriate module
from stack_and_queue.trees.trees import BinarySearchTree 

def test_instantiate_empty_tree():
    tree = BinarySearchTree()
    assert tree.root == None

def test_instantiate_tree_with_single_node():
    tree = BinarySearchTree()
    tree.add(10)
    assert tree.root.value == 10
    assert tree.root.left == None
    assert tree.root.right == None

def test_add_left_and_right_children():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15

def test_pre_order_traversal():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)

    expected_output = [10, 5, 3, 7, 15]
    assert tree.pre_order() == expected_output

def test_in_order_traversal():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)

    expected_output = [3, 5, 7, 10, 15]
    assert tree.in_order() == expected_output

def test_post_order_traversal():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)

    expected_output = [3, 7, 5, 15, 10]
    assert tree.post_order() == expected_output

def test_contains_existing_value():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    assert tree.contains(10) == True
    assert tree.contains(5) == True
    assert tree.contains(15) == True

def test_contains_non_existing_value():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    assert tree.contains(20) == False
    assert tree.contains(7) == False
    assert tree.contains(12) == False