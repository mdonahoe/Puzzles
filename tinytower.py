from random import randint
floors = """
A a
F wakka wok
F taco bill
A b
R bit peddler
A c
S pump butt
S drugs
A d
P sew fab
P books
A e
C cake bitch
R muse
A f
C drink
R blockbust
F scooper
A g
S lies
C glass
A mustache
A beards
P riaa
A hats
S misplaced
F subway
A k
R scammer
C tats
A l
P toy story
A m
R cybercafe
F froyo
A n
A o
S isis
P plaaants
C dress up
F five guys
A shaved
A q
S too big too fail
R volleyball
P candle shop
A r
C ?
"""

floors = [f.split(' ', 1) for f in floors.split('\n') if f]

def score(fs):
    prev = 'A'
    score = 0
    for t,n in fs:
        if t==prev:
            continue
        prev = t
        score+=1
    return score

def swap(a,b,xs,show=False):
    ys = list(xs)
    temp = ys[a]
    ys[a] = ys[b]
    ys[b] = temp
    if show: print 'swapping %s with %s' % (ys[a][1],ys[b][1])
    return ys

def improve(fs):
    while True:
        i = randint(0,len(fs)-1)
        j = randint(0,len(fs)-1)
        if i!=j: break
    gs = swap(i,j,fs)
    if score(gs) < score(fs):
        print 'better'
        return gs, 1
    return fs, 0

def run(fs):
    moves = 0
    s = score(fs)
    t = 0
    while moves < 50 and s > 6 and t<2000:
        t+=1
        fs, incr = improve(fs)
        s = score(fs)
        print s
        moves+=incr
    return score(fs), moves, fs

def evict(arr,fs):
    """see which floors are misplaced"""
    evicted = []
    i= -1
    for desired,actual in zip(arrangement, fs):
        i+=1
        t,n = actual
        if desired == t: continue
        evicted.append(i)
    return evicted

def changeup(arr,fs):
    # who is in the wrong spot
    es = evict(arr,fs)
    swaps = [(fs[i][0],arr[i],i) for i in es]

    saved = set()
    zzz = []
    # find perfect partners
    queue = list(swaps)
    while queue:
        s = queue.pop(0)
        j = s[2]
        if j in saved: continue
        i = findpartner(s,swaps)
        if i is None:
            continue
        zzz.append((i,j))
        saved.add(i)
        saved.add(j)
        swaps = [(fs[i][0],arr[i],i) for i in es if i not in saved]

    # find any partners
    swaps2 = [(fs[i][0],arr[i],i) for i in es if i not in saved]
    queue = list(swaps2)
    while queue:
        s = queue.pop(0)
        j = s[2]
        if j in saved:
            continue
        i = forcepartner(s,swaps2)
        if i is None:
            continue
        saved.add(j)
        saved.add(i)
        zzz.append((i,j))
        swaps2 = [(fs[i][0],arr[i],i) for i in es if i not in saved]

    for i,j in zzz:
        fs = swap(i,j,fs)
    return fs, zzz

def findpartner(x,ys):
    for y in ys:
        if y[1]==x[0] and y[0]==x[1]: return y[2]

def forcepartner(x,ys):
    for y in ys:
        if y[1]==x[0]:
            return y[2]

def doit(arr):
    fs = list(floors)
    swaps = []
    while evict(arr,fs):
        fs,s = changeup(arr,fs)
        swaps.extend(s)
    return swaps

from itertools import permutations
minswaps = range(100000)
allswaps = []
for order in permutations('FSRCP'):
    arrangement = 'A'*18+''.join(o*6 for o in order)
    swaps = doit(arrangement)
    allswaps.append((len(swaps), swaps))

print min(allswaps)
zzz = min(allswaps)[1]
fs = floors
for i,j in zzz:
    fs = swap(i,j,fs,True)
