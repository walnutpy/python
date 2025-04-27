from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

que = deque(i for i in range(1,n+1))

arr = list(map(int,input().split()))

count = 0

def two(q):
    a = q.popleft()
    q.append(a)
    return q

def three(q):
    a = q.pop()
    q.appendleft(a)
    return q
    
count = 0
for i in arr:
    two_que = deque(list(que))
    three_que = deque(list(que))
    two_c = 0
    three_c = 0
    while two_que[0] != i:
        two(two_que)
        two_c += 1
        
    while three_que[0] != i:
        three(three_que)
        three_c+=1
    
    if two_c>= three_c:
        que = three_que
        count += three_c
    else:
        que = two_que
        count += two_c

    que.popleft()

print(count)