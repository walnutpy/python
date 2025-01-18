from collections import deque
import sys
input = sys.stdin.readline
n = input().rstrip()
dq = deque()
for i in n:
    dq.append(int(i))

middle = int(len(dq)/ 2)

left = 0
right = 0

for _ in range(middle):
    left += dq.popleft()
    right += dq.pop()

if left == right:
    print("LUCKY")
else:
    print("READY")