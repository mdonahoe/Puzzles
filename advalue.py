users = [(namer(5), choice([randint(0,999), min(999,pos(int(50*gauss(0,1)))), abs(int(gauss(0,10)))])) for _ in range(100)]
xs = [(b,a) for a,b in users]
zs = (0,5,10,20,50,100,200,500,750,1000)
def group(xs,zs):
    prev = None
    for z in zs:
        print '%s - %s: %s' %(prev, z, ' '.join(b for a,b in xs if a>prev and a<=z))
        prev = z

