"""
Compress words
reduce a list of words into a single string
this string must contain all the words, but they can overlap
"""
inp = ['hello','he','she','longest','strong']
out = 'shellongestrong'

# 1. sort words by size and check for complete inclusion
# this removes 'he'
"""
    she, hello, longest, strong
she  -1,     2,       0,      0,
hello 0,    -1,       2,      0,
lo    0,     0,      -1,      2,
str   0,     0,       0,     -1
"""

words = list(inp)
words.sort(key=len)

included = []
while words:
    w = words.pop()
    for x in included:
        if w in x:
            break
    else:
        included.append(w)

# check for overlaps
def memoize(f):
    cache = {}
    def g(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    g.cache = cache
    return g

@memoize
def overlap(a,b):
    n = len(a)
    m = len(b)
    i = max(n - m, 0)
    while i < n:
        if b.startswith(a[i:]):
            return n - i
        i+=1
    return 0

def overlap_map(included):
    n = len(included)
    M = dict()
    for i,w1 in enumerate(included):
        M[w1] = dict()
        for j,w2 in enumerate(included):
            if i==j: continue
            M[w1][w2] = overlap(w2,w1)
    return M

def one_and_all(xs):
    "iterate over all possible"
    for i in xrange(len(xs)):
        x = xs[i]
        rest = xs[:i] + xs[i+1:]
        yield x, rest

counter = [0]
@memoize
def recurse(words):
    "return the smallest string that contains all words"
    if not words: return ''
    if len(words) == 1: return words[0]
    ys = []
    counter[0]+=1
    for x,xs in one_and_all(words):
        s2 = recurse(tuple(xs))
        if x == 'compare':
            print x, s2
        if x in s2:
            ys.append(s2)
            continue
        n = overlap(x, s2)
        ys.append(x + s2[n:])
    return min(ys, key=len)

def travel(words):
    while words:
        w = words.pop()


if __name__ == '__main__':
    from random import shuffle
    from sys import argv
    ls = argv[1:]
    for i in range(10):
        shuffle(ls)
        x = recurse(tuple(ls))
        print '>',x
