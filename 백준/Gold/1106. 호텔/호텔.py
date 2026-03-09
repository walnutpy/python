c, n = map(int,input().split())
#c target person
#n city option

city = []
for _ in range(n):
    city.append(list(map(int,input().split())))
    
dp = [10**9]*(c+101)
dp[0] = 0
for cost, people in city:
    for i in range(people,c+101):
        dp[i] = min(dp[i],dp[i-people] + cost)
        
ans = 10**9
for i in range(c,c+101):
    ans = min(dp[i],ans)
    
print(ans)