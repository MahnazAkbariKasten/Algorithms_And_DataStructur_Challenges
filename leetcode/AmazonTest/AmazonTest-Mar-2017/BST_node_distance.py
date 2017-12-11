__author__ = 'pretymoon'
# TO BE MODIFIED AS CAN INSERT NODES AFTER TREE HAS BEEN BUILT!!!!!!

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
        self.level = 0
        self.parent = None


class Tree:
    def __init__(self, r):
        self.root = r
        self.size = 0
        self.depth = 0
        self.node_list = None


def binary_insert(root, node):
    if root is None:
        bst_root = node
        node.level = 0
        node_list[value_list[0]] = bst_root
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
                node.level = root.level + 1
                node.parent = root
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
                node.level = root.level + 1
                node.parent = root
            else:
                binary_insert(root.r_child, node)

def build_bst(value_list):
    bst_root = Node(value_list[0])
    node_list[value_list[0]] = bst_root
    for i in range(1, len(value_list)):
        node_list[value_list[i]] = Node(value_list[i])
        binary_insert(bst_root, node_list[value_list[i]])
    return bst_root

def nodes_distance(val1, val2):
    if val1 not in value_list or val2 not in value_list:
        return -1

    node1 = node_list[val1]
    node2 = node_list[val2]
    if node1.level < node2.level:
        m = node2
        n = node1
        # level_m = m.level
        # level_n = n.level
    else:
        m = node1
        n = node2
        # level_n = n.level
        # level_m = m.level

    distance = 0
    c_m_node = m
    c_n_node = n

    # if m.level - n.level > 1:
    for i in range(m.level, n.level + 1, -1):
        distance += 1
        c_m_node = c_m_node.parent

    if n == c_m_node.parent:
        distance += 1
        return distance
    else:
        if c_m_node.level != c_n_node.level:
            distance += 1
            c_m_node = c_m_node.parent

        while c_m_node.parent != c_n_node.parent:
            distance += 2
            c_m_node = c_m_node.parent
            c_n_node = c_n_node.parent

        distance += 2
        return distance


def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)


def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)


value_list = [5, 6, 3, 1, 2, 4, 11, 7]
val1 = 4
val2 = 7

node_list = {}
bst_root = build_bst(value_list)
# pre_order_print(bst_root)
#
# print("="*20)
#
# pre_order_print(node_list[3])
#
# print("="*20)
#
for node in node_list.values():
    print(node.data," ", end='')
    if node.parent == None:
        print("NONE")
    else:
        print(node.parent.data)
#
print("="*20)

print(nodes_distance(val1, val2))