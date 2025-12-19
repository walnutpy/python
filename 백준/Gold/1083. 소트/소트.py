import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
s = int(input())

for i in range(n):
    if s == 0:
        break
    end = min(n-1,i+s)
    
    max_i = i
    for j in range(i+1,end+1):
        if arr[j] > arr[max_i]:
            max_i = j

    for j in range(max_i,i,-1):
        arr[j],arr[j-1] = arr[j-1],arr[j]

    s -= max_i - i

print(*arr)