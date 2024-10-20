a = [1,2,3,4]
b = iter(a)

while True:
    try:
        print(next(b))
    except StopIteration:
        break