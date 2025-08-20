import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(graph, v , visted):
    global cnt 
    visted[v] = True
    count[v-1] = cnt
    cnt += 1

    for i in graph[v]:
        if not visted[i]:
            dfs(graph,i,visted)

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    p,q = map(int,input().split())
    graph[p].append(q)
    graph[q].append(p)

visted = [False] * (n+1)
count = [0] * n
cnt = 1 

for i in (graph):
    i.sort()
dfs(graph,r,visted)

for i in count:
    print(i)