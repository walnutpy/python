import sys
from collections import deque
input = sys.stdin.readline

def draw(num):
    dack = deque(range(1,num + 1))
    while len(dack) > 1:
        dack.popleft()
        dack.append(dack.popleft())
    return dack[0]
n = int(input())
print(draw(n))