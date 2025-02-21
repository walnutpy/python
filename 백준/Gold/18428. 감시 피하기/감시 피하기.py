import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

board = []
t = []
x = []
see = [(1,0),(-1,0),(0,-1),(0,1)]

def teacher_see():
    q = deque(t)
    while q:
        x, y = q.popleft()
        for dx, dy in see:
            cx,cy = x,y
            while True:
                cx += dx
                cy += dy
                if cx < 0 or cx >= n or cy < 0 or cy >= n:
                    break
                if board[cx][cy] == 'O':
                    break
                if board[cx][cy] == 'S':
                    return False
    return True

n = int(input())
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'X':
            x.append((i,j))
        if board[i][j] == 'T':
            t.append((i,j))

#make object
found = False
for c in combinations(x, 3):
        for x,y in c:
            board[x][y] = 'O'
        if teacher_see():
            found = True
            print("YES")
            break
        for x,y in c:
            board[x][y] = 'X'

if not found:
    print("NO")