from collections import deque
import sys
input = sys.stdin.readline
n , m = map(int,input().split())
arr = []
q = []
zero = []
answer = -1
move = [(1,0),(-1,0),(0,1),(0,-1)]

def virus(zero_a):
    tamp = [i[:] for i in arr]
    dq = deque(q)
    a = 0
    while dq:
        x,y = dq.popleft()
        for dx, dy in move:
            next_x = x + dx
            next_y = y + dy
            if 0<=next_x < n and 0<= next_y<m and tamp[next_x][next_y]==0:
                tamp[next_x][next_y] = 2
                dq.append((next_x,next_y))
                a += 1
    return zero_a - a
                

for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(m):
        if arr[i][j] == 0:
            zero.append((i,j))
        elif arr[i][j] == 2:
            q.append((i,j))

for i in range(len(zero)-2):
    for j in range(i+1,len(zero)-1):
        for k in range(j+1,len(zero)):
            c = [zero[i],zero[j],zero[k]]
            for x,y in c:
                arr[x][y] = 1
            zeor_area = len(zero) -3
            answer = max(virus(zeor_area),answer)
            for x, y in c:
                arr[x][y] = 0

print(answer)