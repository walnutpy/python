
def dfs(v, visited):
    visited[v]=True
    for next,p,q in arr[v]:
        if not visited[next]:
            num[next] = num[v]*q
            dens[next]=dens[v]*p
            g = gcd(num[next],dens[next])
            num[next] = num[next]//g
            dens[next] = dens[next] // g
            dfs(next,visited)

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

n = int(input())

#입력형식
#abpq
#a:b=p:q
#필요한 질량을 모두 더한 값 최소
arr=[[] for _ in range(n)]

for _ in range(n-1):
    a,b,p,q=map(int,input().split())
    arr[a].append((b,p,q))
    arr[b].append((a,q,p))

visited = [False]*n

num=[0]*n
dens=[0]*n
num[0]=1
dens[0]=1

dfs(0,visited)

lcm_total=dens[0]
for i in range(n-1):
    lcm_total = lcm(lcm_total,dens[i+1])

for i in range(n):
    num[i] = num[i] * (lcm_total//dens[i])


print(*num)