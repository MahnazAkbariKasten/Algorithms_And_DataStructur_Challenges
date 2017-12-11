__author__ = 'pretty moon'

import node_manipulation as nm




# Driver
a = nm.Node(name="a")
b = nm.Node(name="b")

g = {a, b}

nm.Node.add_neighbour(a, b)
print(nm.graph_connections(g))