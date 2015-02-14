#!/usr/bin/python
import sys
from random import randint


class Node:
    def __init__(self, identifier):
        self.id = identifier
        self.parent = self
        self.num_of_children = 0

    def append_child(self, node):
        node.parent = self
        self.num_of_children += 1

    def __repr__(self):
        return '<Tree node | ID {}, parent ID {}>'.format(self.id, self.parent.id)


def create_tree(size):
    """
    Creates a binary tree with a given number of elements.
    :param size:
    :return: Root element, list of all tree elements.
    """
    root = Node(0)

    current = root

    node_list = []
    global_node_list = [root]

    for i in range(1, size):
        node = Node(i)
        node_list.append(node)
        global_node_list.append(node)
        current.append_child(node)
        if current.num_of_children >= 2:
            current = node_list.pop(0)

    return root, global_node_list


def get_parents_list(node):
    """
    Helper function - creates a list of node's ancestors.
    :param node:
    :return:
    """
    current = node
    parent1 = node.parent
    node_parent_list = [parent1]

    while parent1 != current:
        current = parent1
        parent1 = parent1.parent
        node_parent_list.append(parent1)

    return node_parent_list


def least_common_ancestor_first(node_1, node_2):
    """
    First algorithm implementation.
    First it creates two lists of parents (for node1 and node2).
    Second - it uses double loop to detect first intersection (first common ancestor).
    Complexity - O(N^2) in worst case, where N is height of the tree.
    :param node_1:
    :param node_2:k
    :return:
    """
    node1_parent_list = get_parents_list(node_1)
    node2_parent_list = get_parents_list(node_2)
    steps = 0
    for node in node1_parent_list:
        for node2 in node2_parent_list:
            steps += 1
            if node == node2:
                return node, '{} steps'.format(steps)


def least_common_ancestor_second(node1, node2):
    """
    Second least common ancestor algorithm implementation.
    Complexity is linear (of height of the tree).
    Number of loop executions shouldn't be more than tree height
    :param node1:
    :param node2:
    :return:
    """
    node1_parents = []
    node2_parents = []
    steps = 0
    while True:
        steps += 1
        node1_parents.append(node1)
        node2_parents.append(node2)
        if node1 in node2_parents:
            return node1, '{} steps'.format(steps)
        if node2 in node1_parents:
            return node2, '{} steps'.format(steps)
        node1 = node1.parent
        node2 = node2.parent


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: ./trees.py <number of elemets>, for example: ./trees.py 10000 \n\n')
        sys.exit()

    number_of_elemets = int(sys.argv[1])
    if not number_of_elemets:
        sys.stderr.write('Usage: ./trees.py <number of elemets>, for example: ./trees.py 10000 \n\n')
        sys.exit()

    # create a tree of N items

    sys.stdout.write('Creating a tree of {} elements\n\n'.format(number_of_elemets))
    root, node_list = create_tree(number_of_elemets)

    # just take 2 random nodes
    # to compare number of loop execution using different algorithms
    node1 = node_list[randint(0, number_of_elemets-1)]
    node2 = node_list[randint(0, number_of_elemets-1)]

    parent, steps = least_common_ancestor_first(node1, node2)
    sys.stdout.write('Executing first (square) algorithm took: {}\n\n'.format(steps))

    parent, steps = least_common_ancestor_second(node1, node2)
    sys.stdout.write('Executing second (linear) algorithm took: {}\n\n'.format(steps))