from collections import deque
import sys
input = sys.stdin.readline
n = input().rstrip()
dq = deque()
for i in n:
    dq.append(int(i))
left = 0
right = 0
while len(dq) != 0:
    left += dq.popleft()
    right += dq.pop()

if left == right:
    print("LUCKY")
else:
    print("READY")