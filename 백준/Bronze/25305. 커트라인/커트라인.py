n,k=map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
winer = len(arr) - k
print(arr[winer])