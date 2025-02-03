import math
def factor(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

m = int(input())
n = int(input())
arr = []

for i in range(m, n+1):
    if factor(i):
        arr.append(i)
    
if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)