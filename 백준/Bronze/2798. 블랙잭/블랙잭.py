n,m=map(int,input().split())
arr = list(map(int,input().split()))
lst = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            sum_t = arr[i]+arr[j]+arr[k]
            if sum_t > m:
                continue
            else:
                lst.append(sum_t)
print(max(lst))