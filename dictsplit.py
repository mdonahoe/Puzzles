import sys


words = set(['bad','ba','ad','ab', 'one','a',''])

s = 'abadone'
s = 'abaaaaaz'
def sent(x):
    print x
    if x in words: return True
    L = len(x) - 1
    if L < 1: return False
    i=1
    while i < L:
        if x[:i] in words and sent(x[i:]): return True
        i+=1
    return False
print sent(s)
