import math
n,m = map(int, input().split())

def eratosthenes(m,n):
    arr = [False,False] + [True]*(n-1)
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]:
            j = 2
            while j * i <= n:
                arr[j*i] = False
                j +=1
        
    for i in range(m,n+1):
        if arr[i]:
            print(i)

eratosthenes(n,m)