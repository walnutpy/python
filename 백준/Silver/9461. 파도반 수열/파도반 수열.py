n = int(input())
arr = [0,1,1,1,2,2]
for _ in range(n):
    a = int(input())
    if len(arr)-1 >= a:
        print(arr[a])
        continue
    for i in range(len(arr),a+1):
        arr.append(arr[i-5]+arr[i-1])
    print(arr[a])