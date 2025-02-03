from collections import deque
def factor(a,k):
    i = 1
    deq = deque()
    while i <=a:
        if a % i == 0:
            deq.append(i)
        if len(deq) == k:
            return deq.pop()
        i+=1
    return 0
n , k = map(int,input().split())
print(factor(n,k))