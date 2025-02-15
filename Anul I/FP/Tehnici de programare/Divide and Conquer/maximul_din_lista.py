def maximul(l):
    if len(l) == 0:
        return -1
    if len(l) == 1:
        return l[0]
    middle = len(l) // 2
    return max(maximul(l[:middle]), maximul(l[middle:]))

L = [-3,-2,-5]
print(maximul(L))