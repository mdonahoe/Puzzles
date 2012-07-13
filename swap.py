x = list('abcdef')
N = len(x)
for i in range(N):
    if (i+1)>=N/2: break
    temp = x[i]
    x[i] = x[N-i-1]
    x[N-i-1] = temp 

print x
