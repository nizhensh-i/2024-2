def birnary_search(a: list, l, x, r):
    i = l
    j = r - 1
    while i <= j:
        m = (i + j) // 2
        if a[m] == x:
            return m
        elif x > a[m]:
            i = m + 1
        else:
            j = m - 1
    return -1


array = [1,10,18,9,78,89,100]
position = birnary_search(array, 0, 89, 7)
print(position)
