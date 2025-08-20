import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
count=1
def dfs(graph,v,visited):
    global count
    visited[v] = count
    for i in graph[v]:
        if visited[i] == 0:
            count +=1
            dfs(graph,i,visited)

n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    u,v= map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for k in graph:
    k.sort()

visited = [0]*(n+1)

dfs(graph,r,visited)

for j in range(1,n+1):
    print(visited[j])