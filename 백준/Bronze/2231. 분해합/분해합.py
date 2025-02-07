n = int(input())
arr =[]
for i in range(1,n+1):
    sum_all = sum(map(int,str(i)))
    if i + sum_all == n:
        arr.append(i)
if arr:
    print(min(arr))
else:
    print(0)