a = int(input())
n = list(map(int,input().split()))
arr = [0]
for i in n:
    if i > arr[-1]:
        arr.append(i)
    else:
        start,end= 0,len(arr)-1
        while start < end:
            mid = (start+end)//2
            if i <= arr[mid]:
                end = mid
            else:
                start = mid +1
        arr[start] = i
print(len(arr)-1)