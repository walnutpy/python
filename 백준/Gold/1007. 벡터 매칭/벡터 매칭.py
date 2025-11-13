import math
from itertools import combinations

T = int(input())
for _ in range(T):
    n = int(input())

    arr = []
    t_x = 0
    t_y = 0

    for i in range(n):
        x,y = map(int,input().split())
        t_x += x
        t_y += y
        arr.append([x,y])
    res = float("INF")
    for comb in combinations(arr,n//2):
        copy_x = t_x
        copy_y = t_y
        for x,y in comb:
            copy_x -= 2*x
            copy_y -= 2*y
        res = min(res,math.sqrt(copy_x**2+copy_y**2))
    print(res)