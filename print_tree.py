"""
Draw a binary tree in ASCII, given the root.
"""
import math
from random import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = chr(value + 65)
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node({}, {}, {})'.format(self.value, self.left, self.right)

    @staticmethod
    def make(value, num_nodes):
        if num_nodes <= 0:
            return None
        left_nodes = math.ceil((num_nodes - 1) / 2.0)
        right_nodes = math.floor((num_nodes - 1) / 2.0)
        left = Node.make(value * 2 + 1, left_nodes)
        right = Node.make((value + 1) * 2, right_nodes)
        return Node(value, left, right)

    @staticmethod
    def random(prob, depth):
        if depth <= 0:
            return None
        if random() < prob:
            return None

        left = Node.random(prob, depth - 1)
        right = Node.random(prob, depth - 1)

        return Node(int(26 * random()), left, right)


def print_tree(node):
    if not node:
        return []

    # Get the fully draw subtrees.
    left = print_tree(node.left)
    right = print_tree(node.right)

    # Combine the subtrees, bottom-up row by row, adding padding.
    output = []
    while left or right:
        a = left and left.pop(0) or " "
        b = right and right.pop(0) or " "
        p = padding(a, b)
        output.append(p)

    if output:
        # Add the structure that joins the subtrees to the root
        full_width = len(output[-1])
        half_width = (full_width - 1) / 2
        quarter_width = (half_width - 1) / 2
        space = " " * quarter_width
        line = "-" * quarter_width
        # Create the horizontal line that joins the subtrees
        output.insert(0, '+'.join((space, line, line, space)))

        # Create the vertical line that goes to the root
        output.insert(0, (2 * space) + " | " + (2 * space))

        # Add the root in the middle.
        output.insert(0, (2 * space) + " %s " % node.value + (2 * space))
    else:
        # Just add the root.
        output.insert(0, node.value)

    return output


def padding(left, right):
    "Pad the shorter string until both are the same size, then join them together."
    diff = len(right) - len(left)
    spaces = " " * (abs(diff) // 2)
    if diff > 0:
        # left is shorter
        left = spaces + left + spaces
    else:
        # right is shorter
        right = spaces + right + spaces

    # Join with an extra space.
    return left + " " + right

full_tree = Node.make(0, 31)
print '\n'.join(print_tree(full_tree))

random_tree = Node.random(0.25, 5)
print '\n'.join(print_tree(random_tree))
