"""
Split a string into a list of valid words
"""
import sys

words = file('/usr/share/dict/words').read().split('\n')
words = set(x for x in words if len(x) > 1)
words.update(['i', 'a'])

def sentence(x):
    if x in words:
        return [x]
    L = len(x) - 1
    if L < 1:
        return []
    i = 1
    while i < L:
        s = sentence(x[i:])
        if x[:i] in words and s:
            return [x[:i]] + s
        i += 1
    return []

print sentence(sys.argv[1].lower())
