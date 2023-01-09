from typing import Generic, Self, TypeVar, Union, List
from itertools import chain
from collections import deque

T = TypeVar('T')


class BST:
    value: Generic[T]
    right: Self
    left: Self

    def __init__(
            self,
            initial_value: Generic[T],
            left: Union[Self, None] = None,
            right: Union[Self, None] = None
    ):
        self.value = initial_value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    @staticmethod
    def depth_first_traversal_iterative(node: Self | None) -> List[T]:
        output = []

        if node is None:
            return output

        stack = [node]
        while len(stack) > 0:
            current = stack.pop()
            output.append(current.value)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

        return output

    @staticmethod
    def breadth_first_traversal_iterative(node: Self | None) -> List[T]:
        output = []

        if node is None:
            return output

        queue = deque([node])

        while len(queue) > 0:
            current = queue.pop()
            output.append(current.value)

            if current.left:
                queue.appendleft(current.left)

            if current.right:
                queue.appendleft(current.right)

        return output

    @staticmethod
    def depth_first_traversal_recursive(node: Self | None) -> List[T]:
        output = []

        if node is None:
            return output

        left_result = BST.depth_first_traversal_recursive(node.left)
        right_result = BST.depth_first_traversal_recursive(node.right)

        return list(chain(node.value, left_result, right_result))

    @staticmethod
    def find_value_in_tree(value: T, node: Self | None) -> bool:
        is_char_present = False

        if node is None:
            return is_char_present

        queue = deque([node])

        while len(queue) > 0:
            current = queue.pop()
            if current.value == value:
                is_char_present = True
                break

            if current.left:
                queue.appendleft(current.left)

            if current.right:
                queue.appendleft(current.right)

        return is_char_present
