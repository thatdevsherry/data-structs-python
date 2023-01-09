from .binary_tree import BST
import pytest


@pytest.fixture
def root_node_of_binary_tree() -> BST:
    a = BST('a')
    b = BST('b')
    c = BST('c')
    d = BST('d')
    e = BST('e')
    f = BST('f')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def test_depth_first_traversal_recursive(root_node_of_binary_tree):
    expected = ['a', 'b', 'd', 'e', 'c', 'f']
    result = BST.depth_first_traversal_recursive(root_node_of_binary_tree)
    assert result == expected


def test_depth_first_traversal_recursive_empty_tree():
    expected = []
    result = BST.depth_first_traversal_recursive(None)
    assert result == expected


def test_depth_first_traversal_iterative(root_node_of_binary_tree):
    expected = ['a', 'b', 'd', 'e', 'c', 'f']
    result = BST.depth_first_traversal_iterative(root_node_of_binary_tree)
    assert result == expected


def test_depth_first_traversal_iterative_empty_tree():
    expected = []
    result = BST.depth_first_traversal_iterative(None)
    assert result == expected


def test_breadth_first_traversal_iterative(root_node_of_binary_tree):
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    result = BST.breadth_first_traversal_iterative(root_node_of_binary_tree)
    assert result == expected


def test_find_char_in_tree(root_node_of_binary_tree):
    char, expected = 'a', True
    result = BST.find_char_in_tree(char, root_node_of_binary_tree)
    assert result == expected


def test_failing_find_char_in_tree(root_node_of_binary_tree):
    char, expected = 'this is nice', False
    result = BST.find_char_in_tree(char, root_node_of_binary_tree)
    assert result == expected
