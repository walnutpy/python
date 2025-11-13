import sys
import math
input = sys.stdin.readline
#dist-이동해야할 거리
#max_n - 한 이동에서 최대로 이동할 수 있는 거리
#c - 이동 횟수
def fly(x,y):
    dist = y -x
    max_n = int(math.sqrt(dist))
    c = 2*(max_n) - 1   
    if dist == max_n**2:
        print(c)
        return
    dist_s = max_n ** 2
    if dist <= dist_s + max_n:
        print(c+1)
    else:
        print(c+2)


T = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    fly(x,y)