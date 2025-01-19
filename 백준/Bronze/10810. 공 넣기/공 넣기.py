import sys
input = sys.stdin.readline

n, m = map(int, input().split())
count = [0]*n
for _ in range(m):
    i, j, k = map(int,input().split())
    for i in range(i-1, j):
        count[i] = k

print(*count)