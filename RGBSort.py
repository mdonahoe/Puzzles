import random
class ColorObj:
    colors = ['R', 'G', 'B']
    def __init__(self):
        self.color = random.choice(ColorObj.colors)
    def __repr__(self):
        return self.color

def mattsort(a, colors, c=0, i=0):
    if c >= len(colors) - 1: return
    for j in xrange(i, len(a)):
        if a[j].color != colors[c]: continue
        a[i], a[j], i = a[j], a[i], i + 1
    mattsort(a, colors, c + 1, i)

a = [ColorObj() for _ in range(20)]
print 'start:', a
mattsort(a, colors=ColorObj.colors)
print '  end:', a

