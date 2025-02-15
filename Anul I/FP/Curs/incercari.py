def f(l):
    if len(l) == 0:
        return -1
    
    if len(l) == 1:
        return l[0]
    
    middle = len(l) // 2
    st = f(l[:middle])
    dr = f(l[middle:])

    return max(st, dr)

print(f([1, 2, 11, 4, 5, 6, 7, 8, 9]))
