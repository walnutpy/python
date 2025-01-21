n = int(input())
count = 0
for i in range(n):
    s = input()
    arr=[]
    group = True
    back = None
    for j in s:
        if j != back:
            if j in arr:
                group = False
                break
            arr.append(j)
        back = j
    if group:
        count +=1
print(count)