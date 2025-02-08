import sys


def find_cyclic_path(n: int, m: int) -> list[int]:
    if n == 0:
        return []
    i = 1
    res = []
    while True:
        res.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    return res

n, m = map(int, sys.argv[1:3])
print(''.join(map(str, find_cyclic_path(n, m))))
