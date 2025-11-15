from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    dq = deque(map(str,input().split()))
    string = dq.popleft()
    while dq:
        i = dq.popleft()
        left = i + string 
        right = string + i
        if left < right:
            string = left
        else:
            string = right
    print(string)