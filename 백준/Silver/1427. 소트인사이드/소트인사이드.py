n = input()
arr =[]
for i in n:
    arr.append(i)
arr.sort(reverse=True)
for i in arr:
    print(i,end='')