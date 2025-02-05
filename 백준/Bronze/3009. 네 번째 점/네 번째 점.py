arr_x = set()
arr_y = set()
for _ in range(3):
    x,y = map(int,input().split())
    if x in arr_x:
        arr_x.remove(x)
    else:
        arr_x.add(x)
    if y in arr_y:
        arr_y.remove(y)
    else:
        arr_y.add(y)
print(*arr_x,*arr_y)