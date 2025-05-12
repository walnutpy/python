from collections import deque
n, k = map(int,input().split())
que = deque(i for i in range(1,n+1))
arr =[]
while que:
    for _ in range(k-1):
        que.append(que.popleft())
    a = que.popleft()
    arr.append(a)
print('<', end= '')
for i in range(n):
    if i == n-1:
        print(arr[i], end='>')
    else:
        print(arr[i],end=', ')