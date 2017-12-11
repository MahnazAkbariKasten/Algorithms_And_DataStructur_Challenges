__author__ = 'pretty moon'
# File classtools.py
"Assorted class utilities and tools"

class AttrDisplay:
    """
    Provides and inheritable display overload method that shows instances with their class names and
    name=value pair for each attribute stored on the instance itself(but not attributes inherited from
    its classes). Can be mixed into any class, and will work in any instance.
    """
    def gatherAttrs(self):
        attr = []
        for key in sorted(self.__dict__):
            attr.append("%s=%s" % (key, getattr(self, key)))
        return ", ".join(attr)


    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':
    class simpleNode(AttrDisplay):
        def __init__(self, key, value=None, parent=None, children=None):
            self.key = key
            self.value = value
            self.parent = parent
            self.children = children


    class tree(AttrDisplay):
        def __init__(self, root):
            self.root = root

        def __len__(self):
            treeLen = 0
            return treeLen


    node1 = simpleNode(1)
    node2 = simpleNode(2, "node2", node1)

    tree1 = tree(node1)

    print(node1)
    print(node2)
    print(len(tree1))
