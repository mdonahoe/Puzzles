class Node(object):
    def __init__(self, x, left, right):
        self.x = x
        self.left = left
        self.right = right
    def LCA(self, a, b):
        nodes = self.traverse()
        lca = None
        lca_level = None
        for value, level in nodes:
            if lca is None:
                if value in (a, b):
                    lca_level = level
                    lca = value
            else:
                if lca_level > level:
                    lca_level = level
                    lca = value
                if value in (a, b):
                    return lca
        return None
    def traverse(self, level=0):
        nodes = []
        if self.left:
            nodes.extend(self.left.traverse(level+1))
        nodes.append((self.x, level))
        if self.right:
            nodes.extend(self.right.traverse(level+1))
        return nodes
    def __str__(self):
        return str(self.x)

A = Node('a', None, None)
C = Node('c', None, None)
E = Node('e', None, None)
H = Node('h', None, None)

D = Node('d', C, E)
B = Node('b', A, D)

I = Node('i', H, None)
G = Node('g', None, I)

F = Node('f', B, G)

print ''.join((str(n) for n in F.traverse()))

