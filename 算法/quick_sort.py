def partition(a: list, l, r):
    i = l+1
    j = r
    x = a[l]
    while True:
        while a[i] < x and i < r:
            i += 1
        while a[j] > x:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[l],a[j] = a[j],a[l]
    return j


def quick_sort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quick_sort(a, l, q - 1)
        quick_sort(a, q + 1, r)


a = [23, 100, 67, 2, 100, 9, 2]
quick_sort(a, 0, len(a) - 1)
print(a)
