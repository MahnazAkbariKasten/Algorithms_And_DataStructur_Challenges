__author__ = 'pretty moon'

'''

'''


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.neighbours = []
        self.weight = 1

    def get_name(self):
        return self.name

    def add_neighbour(self, node):
        self.neighbours.append(node)
        return self. neighbours

    def get_neighbours(self):
        return self.neighbours

    def mark_as_visited(self):
        self.visited = True
        return self.visited

    def check_if_visited(self):
        return self.visited

    def mark_as_not_visited(self):
        self.visited = False
        return self.visited

    def list_neighbours(self):
        return [x.get_name() for x in self.get_neighbours()]

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight
        return self.weight


class Root(Node):
    def __init__(self, root):
        self.root = root


def can_reach(node1, node2):
    if node2 in node1.get_neighbours():
        return True
    for neighbour in node1.get_neighbours():
        if not neighbour.check_if_visited():
            neighbour.mark_as_visited()
            if can_reach(neighbour, node2):
                return True
    return False


def one_way_connected_pairs_driver(node1, node2):
    """
    This method checks the one way connectivity which means it checks if node2 can be reached from node1 or the way.
    :param node1:
    :param node2:
    :return: True or False which means reachable or not
    """
    if can_reach(node1, node2) or can_reach(node2, node1):
        return True
    return False


def two_way_connected_pairs_driver(node1, node2):
    """

    :param node1:
    :param node2:
    :return:
    """
    if can_reach(node1, node2) and can_reach(node2, node1):
        return True
    return False


def reset_graph(graph):
    for node in graph:
        node.mark_as_not_visited()


def graph_connections(graph):
    connections = {}
    for node in graph:
        connections[node.get_name()] = node.list_neighbours()
    return connections


def matrix_to_list(matrix):
    '''
    Given an adjacency matrix this module builds a graph in form of an adjacency list and returns the list of nodes.
    :param matrix:
    :return:
    '''
    adjacency_list = {}
    for i in range(len(matrix)):
        neighbours = []

        adjacency_list[i] = neighbours
    return adjacency_list.keys()

# def is_acyclic(root):



