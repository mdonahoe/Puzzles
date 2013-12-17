class Node:
    def __init__(self, value, left=None, right=None):
        self.value = chr(value + 65)
        self.left = left
        self.right = right
    @staticmethod
    def make(n=16, i=1):
        if i >= n: return None
        return Node(i - 1, Node.make(n,i*2), Node.make(n, i*2 + 1))


def print_tree_2(node):
    if not node: return []
    left = print_tree(node.left)
    right = print_tree(node.right)
    x = []
    while left or right:
        a = left and left.pop() or " "
        b = right and right.pop() or " "
        x.append(padd(a,b))
    if x:
        n = len(x[-1])
        m = (n - 1) / 2
        l = (m - 1) / 2
        s = " " * l
        t = "-" * l
        x.append(s + '+' + t + '+' + t + '+' + s)
        x.append((2*s) + " | " + (2*s))
        x.append((2*s) + " %s " % node.value + (2*s))
    else:
        x.append(node.value)
    return list(reversed(x))

def print_tree(node):
    if not node: return []
    left = print_tree(node.left)
    right = print_tree(node.right)
    x = []
    while left or right:
        a = left and left.pop() or " "
        b = right and right.pop() or " "
        x.append(padd(a,b))
    if not x: return [node.value]
    n = len(x[-1])
    m = ((n - 1) / 2 - 1) / 2
    while m < n / 2:
        s = n * [" "]
        s[m] = "/"
        s[-m-1] = "\\"
        x.append(''.join(s))
        m += 1
    s = n * [" "]
    s[n//2] = node.value
    x.append(''.join(s))
    x.reverse()
    return x




"""
      /
     F
    /
   /
  D
 / \
A   B
 +-+-+
 |
 c
+++ +++
| |
a b
"""

def padd(a,b):
    d = len(b) - len(a)
    s = " " * (d//2)
    if d > 0:
        a = s + a + s
    else:
        b = s + b + s
    return a + " " + b
root = Node.make(64)
print '\n'.join(print_tree(root))

