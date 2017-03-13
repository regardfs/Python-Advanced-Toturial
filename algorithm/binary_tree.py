"""
https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%8F%89%E6%A0%91
"""
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v :
            return node
        elif val < node.v and node.l is not None:
            self._find(val, node.l)
        elif val > node.v and node.r is not None:
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

