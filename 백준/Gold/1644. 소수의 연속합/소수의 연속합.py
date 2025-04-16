import math

n = int(input())

def eratosthenes(n):
    ar = [False,False] + [True]*n
    for i in range(2,int(math.sqrt(n))+1):
        if ar[i]:
            j = 2
            while j * i <= n:
                ar[j*i] = False
                j +=1

    arr = [i for i in range(n+1) if ar[i]]

    l = len(arr)
    i = 0
    j = 0
    count = 0
    total = 0
    while True:
        if total > n:
            total -=arr[i]
            i += 1
        elif j == l:
            break
        else:
            total += arr[j]
            j += 1

        if total == n:
            count +=1

    print(count)

eratosthenes(n)
