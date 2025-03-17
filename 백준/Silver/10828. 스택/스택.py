from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
que = deque()

for _ in range(n):
    a = input().split()

    if a[0] == "push":
        que.append(int(a[1]))
    if a[0] == "pop":
        print(que.pop() if que else -1)
    if a[0] == "size":
        print(len(que))
    if a[0] == "empty":
        print(0 if que else 1)
    if a[0] == "top":
        print(que[-1] if que else -1)