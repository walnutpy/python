n,m = map(int,input().split())
arr = list(map(int,input().split()))

min_tree = 1
max_tree = max(arr)

while min_tree <= max_tree:
    mid = (min_tree+max_tree)//2
    length = sum(i - mid for i in arr if i > mid)
    if length >= m:
        min_tree = mid+1
    else:
        max_tree = mid-1

print(max_tree)