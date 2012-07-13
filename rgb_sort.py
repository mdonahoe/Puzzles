class Item(object):
    def __init__(self, hidden):
        self.hidden = hidden
        self.color = choice(range(3))
    def __str__(self):
        return str(self.color)
#        return '%s (%s)' % (self.color, self.hidden)
    def __repr__(self):
        return str(self)

from random import choice


xs = [Item(i) for i in range(20)]
print xs
def sort1(xs):
    totals = [0 for _ in range(1 + max(x.color for x in xs))]
    for x in xs:
        totals[x.color] += 1
    starts = [0]
    for i in range(1, len(totals)):
        starts.append(starts[i-1] + totals[i-1])
    # this is still hard-coded for 3
    ends = [starts[1], starts[2], len(xs)]
    nexts = list(starts)
    i = 0
    while i < len(xs):
        x = xs[i]
        if i >= starts[x.color] and i < ends[x.color]:
            i+=1
            continue
        # move it to where it belongs
        j = nexts[x.color]
        xs[j], xs[i] = xs[i], xs[j]
        nexts[x.color] += 1
    return xs
sort1(xs)
print xs
