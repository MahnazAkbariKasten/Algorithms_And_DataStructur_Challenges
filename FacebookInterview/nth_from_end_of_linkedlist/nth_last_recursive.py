__author__ = 'pretymoon'

class Node:
    def __init__(self, node_value, next_node):
        self.next_node = next_node
        self.node_value = node_value

    def set_next_node(self, new_node):
        next_node = self.new_node

    def get_next_node(self):
        return self.next_node

    def set_data(self, val):
        node_value =self.val

    def get_data(self):
        return self.node_value

def nth_last_node(head, n):
    if head is None:
        return 0
    else:
        tmp = nth_last_node(head.get_next_node(), n) - 1
        if tmp == (-1) * n:
            print(head.get_data())
        return tmp

node3 = Node('three', None)
node2 = Node('two', node3)
node1 = Node('one', node2)

nth_last_node(node1,1)
