def pizza(slices):
    if not slices: return 0
    left = pizza(slices[1:])
    right = pizza(slices[:-1])
    return max((slices[0] - left, 'Left'), (slices[-1]-right, 'Right'))

print pizza([2])
print pizza([1,1,2,1,1])
print pizza([10,100,1,1]), 'R'
print pizza([10,1,1,1])
