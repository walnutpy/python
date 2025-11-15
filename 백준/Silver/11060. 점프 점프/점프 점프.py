from collections import deque

def jump(arr):
    global dp
    que = deque(arr)
    k=0
    dp[0] = 0
    while que and k < len(dp):
        i = que.popleft()
        for j in range(1,i+1):
            if k+j >= len(dp):
                break
            if dp[k] + 1 < dp[k+j]:
                dp[k+j] = dp[k]+1
        k+=1

n = int(input())
arr = list(map(int,input().split()))
dp = [float("INF")]*n
jump(arr)
print(dp[-1] if dp[-1] != float("INF") else -1)