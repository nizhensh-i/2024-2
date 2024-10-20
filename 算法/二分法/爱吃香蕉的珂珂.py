def is_speed_ok(piles: list, speed, h):
    need_hours = 0
    for num in piles:
        need_hours += (num // speed) + 1
    return need_hours <= h


def min_speed(piles, h):
    l = 1
    r = max(piles)
    while l <= r:
        speed = (l + r) // 2
        if l == r:
            return r
        elif is_speed_ok(piles, speed, h):
            r = speed
        else:
            l = speed + 1

    return -1


# piles = [3, 6, 7, 11]
piles = [30, 11, 23, 4, 20]
speed = min_speed(piles, 5)
print(speed)


