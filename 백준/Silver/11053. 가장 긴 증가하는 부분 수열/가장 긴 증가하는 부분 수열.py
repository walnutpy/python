import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
def lis(arr):
    a = len(arr)
    dp = [1]*n
    for i in range(a):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[j]+1,dp[i])
    return max(dp)

print(lis(num))