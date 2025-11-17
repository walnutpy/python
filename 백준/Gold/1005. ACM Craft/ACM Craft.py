from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n,k = map(int,input().split())

    timetable = [0] *(n+1)
    grap = [[]for i in range(n+1)]
    indegree = [0]*(n+1)
    time = list(map(int,input().split()))

    for i in range(k):
        x,y = map(int,input().split())
        grap[x].append(y)
        indegree[y]+=1

    q = deque()
    w = int(input())

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        timetable[node] += time[node-1]
        if node == w:
            break
        for nxt in grap[node]:
            if timetable[nxt] < timetable[node]:
                timetable[nxt] = timetable[node]
            indegree[nxt]-=1
            if indegree[nxt] == 0:
                q.append(nxt)
        

    print(timetable[w])