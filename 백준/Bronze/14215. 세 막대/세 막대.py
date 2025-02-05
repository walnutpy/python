arr = list(map(int,input().split()))
not_triangle = True
while not_triangle:
    max_num = max(arr)
    if max_num<(sum(arr)-max_num):
        not_triangle=False
    else:
        arr.remove(max_num)
        arr.append(max_num -1)

print(sum(arr))