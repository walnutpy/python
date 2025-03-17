from collections import deque 
k = int(input())
sum_ = deque()
for _ in range(k):
    n = int(input())
    if n != 0:
        sum_.append(n)
    else:
        sum_.pop()

print(sum(sum_))