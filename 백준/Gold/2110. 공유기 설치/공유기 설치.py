import sys
input = sys.stdin.readline
n,c=map(int,input().split())
x_arr =[]
for _ in range(n):
    x_arr.append(int(input()))
x_arr.sort()
start_h , end_h = 1, x_arr[-1] -x_arr[0]

while start_h <= end_h:
    mid = (start_h + end_h)//2
    house = x_arr[0]
    count = 1
    for i in range(1,len(x_arr)):
        if x_arr[i] >= house + mid:
            count +=1
            house = x_arr[i]
        
    if count >= c:
        start_h = mid +1
    else:
        end_h = mid -1
print(end_h)