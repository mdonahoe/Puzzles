import random
import Image, ImageDraw

class Vector(tuple):
#    def __new__(cls, *args):
#        return tuple.__new__(cls, args)
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("vectors must be same length")
        return Vector([x+y for x,y in zip(self, other)])
    def __sub__(self, other):
        return self + (-1*other)
    def __mul__(self, c):
        if not isinstance(c, type(1.0)) and \
            not isinstance(c, type(1)):
            raise ValueError("can only multiply a vector by a scalar")
        return Vector([c*x for x in self])
    def __rmul__(self, c):
        return self.__mul__(c)
    def __getattr__(self, attr):
        xyz = dict(x=0, y=1, z=2)
        v = Vector([self[xyz[c]] for c in attr])
        if len(v) == 1:
            v = v[0]
        return v

def mag(a,b):
    dx = a.x - b.x
    dy = a.y - b.y
    return dx*dx+dy*dy

class Viz(object):
    def __init__(self):
        self.im = Image.new("RGB", (300,300), "#FFFFFF")
        self.draw = ImageDraw.Draw(self.im)
    def point(self, center, r=10, fill=(255, 0, 0)):
        x, y = center
        self.draw.ellipse((x-r, y-r, x+r, y+r), fill=fill)
    def connect(self, a, b, width=5, fill=(0,0,0)):
        self.draw.line([a, b], width=width, fill=fill)
    def save(self, filename="out.png"):
        self.im.save(filename, "PNG")

def minspan(pts):
    q = pts[:]
    g = [q.pop()]
    es = []
    while q:
        a = q.pop()
        b = min((mag(a,x),x) for x in g)[1]
        es.append((a,b))
        g.append(a)
    return es

def minspan2(pts):
    es = [(mag(a,b),(a,b)) for a in pts for b in pts if a!=b]
    es.sort()
    g = set()
    g.add(es[0][1][0])
    outs = []
    while es:
        _,e = es.pop(0)
        a,b = e
        if a in g:
            if b in g:
                continue
            g.add(b)
            outs.append(e)
        else:
            if b not in g:
                es.append((0,e))
                continue
            g.add(a)
            outs.append(e)
    return outs

def minspan4(pts):
    es = [(mag(a,b),(a,b)) for a in pts for b in pts if a!=b]
    es.sort()
    g = set()
    g.add(es[0][1][0])
    outs = []

def minspan5(pts):
    q = dict(enumerate(pts))
    g = [q.pop(0)]
    es = []
    while q:
        d,a,k = min((mag(a,b),a,k) for a in g for k,b in q.iteritems())
        b = q.pop(k)
        es.append((a,b))
        g.append(b)
    return es

def minspan3(pts):
    # hi there
    pass


def prims(nodes):
    start = nodes[0]
    Q = set([start])
    S = set(nodes[1:])
    D = [(mag(node,start),(node,start)) for node in Q]
    while Q:
        dist = 10e20
        shortest = None
        for d, e in D:
            if d > dist: continue
            dist,shortest = d,e
        node, _ = shortest
        E.append(shortest)
        S.add(node)
        Q.remove(node)
        D.remove(index)






rr = lambda c: int(c*random.random())

import sys
N = int(sys.argv[1])
pts = [Vector((rr(300),rr(300))) for _ in range(N)]
v = Viz()
for p in pts:
    v.point(p)
edges = minspan5(pts)
for i,(a,b) in enumerate(edges): v.connect(a,b, 3)
v.save()

