import pytest
from tree_intersection.tree_intersection import  BinarySearchTree,tree_intersection

def test_tree_intersection():

    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(5)
    tree1.add(2)
    tree1.add(8)
    tree1.add(1)
    tree1.add(3)
    tree2.add(7)
    tree2.add(2)
    tree2.add(9)
    tree2.add(1)
    tree2.add(4)

    common_values = tree_intersection(tree1, tree2)
    expected_result = [1, 2]
    assert common_values == expected_result




