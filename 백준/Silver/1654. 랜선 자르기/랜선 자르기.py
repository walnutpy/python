import sys
input = sys.stdin.readline
k,n = map(int,input().split())
arr = []
for i in range(k):
    arr.append(int(input()))
#더 필요한 랜선의 수 n-k
min_len = 1
max_len = max(arr)
while min_len <= max_len:
    mid = (min_len+max_len)//2
    count = 0
    for i in arr:
        count += i // mid
    if count >= n:
        min_len = mid+1
    else:
        max_len = mid-1

print(max_len)