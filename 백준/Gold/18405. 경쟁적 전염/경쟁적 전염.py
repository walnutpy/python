import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
arr = []
q = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(n):
        if arr[i][j] > 0:
            q.append((arr[i][j], i, j, 0)) #바이러스 수, x좌표, y좌표, 초

q = deque(sorted(q, key=lambda x: x[0]))
s,x,y = map(int,input().split())
move = [(1,0),(0,1),(-1,0),(0,-1)]

while q:
    num, i, j, second = q.popleft()
    if second == s:
        break
    for p_x, p_y in move:
        next_i = i + p_x
        next_j = j + p_y
        if 0<=next_i<n and 0<=next_j<n and arr[next_i][next_j] ==0:
            arr[next_i][next_j] = num
            second+=1
            q.append((arr[next_i][next_j],next_i,next_j,second))

print(arr[x-1][y-1])