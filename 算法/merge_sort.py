
# 归并排序
def merge(a: list, b: list, l, m, r):
    i = l
    j = m + 1
    z = l
    while i <= m and j <= r:
        if a[i] >= a[j]:
            b[z] = a[j]
            z += 1
            j += 1
        else:
            b[z] = a[i]
            z += 1
            i += 1
    while i <= m:
        b[z] = a[i]
        z += 1
        i += 1
    while j <= r:
        b[z] = a[j]
        z += 1
        j += 1
    for k in range(l, r + 1):
        a[k] = b[k]


def merge_sort(a, b, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(a, b, l, m)
        merge_sort(a, b, m + 1, r)
        merge(a, b, l, m, r)


a = [98, 23, 10, 100, 4, 14, 9]
b = [0]*len(a)
merge_sort(a, b, 0, len(a)-1)
print(a)
