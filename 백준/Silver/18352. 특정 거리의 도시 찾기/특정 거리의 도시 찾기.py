from collections import deque
import sys

input = sys.stdin.readline

n, m , k ,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

def bfs(g, node, visited):
    que = deque([node])
    visited[node] = True
    dist = [-1]*(n+1)
    dist[node] = 0
    while que:
        v = que.popleft()
        for i in g[v]:
            if not(visited[i]):
                que.append(i)
                visited[i]=True
                dist[i] = dist[v] + 1
    return dist

visited = [False]*(n+1)

l = bfs(graph,x,visited)
city = [i for i in range(1,n+1) if l[i] == k]
city.sort()
if city:
    for i in city:
        print(i)
else:
    print(-1)