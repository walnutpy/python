import math
mini,maxi=map(int,input().split())
l=maxi-mini+1
arr=[True]*(l)

for i in range(2,int(math.sqrt(maxi)+1)):
    sq = i * i
    start=((mini+sq-1)//sq)*sq
    for j in range(start,maxi+1,sq):
        arr[j-mini]=False
print(sum(arr))