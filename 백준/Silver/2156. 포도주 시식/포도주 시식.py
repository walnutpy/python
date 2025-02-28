n = int(input())
arr = [int(input()) for _ in range(n)]

#dp[n] = max(dp[n-3] + arr[n] + arr[n-1], dp[n-2]+arr[n], dp[n-1])

dp = [0]*(n)
dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0]+arr[1]
if n > 2:
    dp[2] = max(arr[0]+arr[2],arr[1]+arr[2],dp[1])
    for i in range(3,n):
        dp[i] = max(dp[i-3] + arr[i] + arr[i-1], dp[i-2]+arr[i], dp[i-1])
print(dp[n-1])