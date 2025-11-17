from collections import deque
n = int(input())
timetable = [0] * (n+1)
indegree = [0]*(n+1)
time = [0]*(n+1)
graph = [[]for _ in range(n+1)]
for i in range(1,n+1):
    arr = list(map(int,input().split()))
    time[i] = arr[0]
    for j in arr[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

dq = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        dq.append(i)

while dq:
    node = dq.popleft()
    timetable[node] += time[node]

    for nxt in graph[node]:
        if timetable[nxt] < timetable[node]:
            timetable[nxt] = timetable[node]
        indegree[nxt] -= 1
        if indegree[nxt] ==0:
            dq.append(nxt)

for i in range(1,n+1):
    print(timetable[i])