# How does merge sort work?

def mergesort(xs):
    "My first attempt at merge sort."
    n = len(xs) // 2
    if n < 1:
        return xs
    ys = mergesort(xs[:n])
    zs = mergesort(xs[n:])
    i = 0
    j = 0
    out = []
    while i < len(ys) and j < len(zs):
        if ys[i] < zs[j]:
            x = ys[i]
            i += 1
        else:
            x = zs[j]
            j += 1
        out.append(x)
    out.extend(ys[i:])
    out.extend(zs[j:])
    return out


xs = [3,4,6,8,45,3,4,6]

print mergesort(xs)
