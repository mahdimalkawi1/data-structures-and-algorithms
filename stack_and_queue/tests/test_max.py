import pytest
from stack_and_queue.queue import Queue
from stack_and_queue.trees.trees import BinarySearchTree, Tnode

def test_max_value():
    tree = BinarySearchTree()
    tree.root = Tnode(10)
    tree.root.left = Tnode(5)
    tree.root.right = Tnode(8)
    assert tree.max_value() == 10

    tree = BinarySearchTree()
    tree.root = Tnode(20)
    tree.root.left = Tnode(50)
    tree.root.left.left = Tnode(25)
    tree.root.left.right = Tnode(30)
    tree.root.right = Tnode(15)
    assert tree.max_value() == 50

    tree = BinarySearchTree()
    tree.root = Tnode(10)
    tree.root.left = Tnode(5)
    tree.root.right = Tnode(15)
    tree.root.right.left = Tnode(12)
    tree.root.right.right = Tnode(18)
    assert tree.max_value() == 18

