n = int(input())
arr = []
while n != 1:
    i = 2
    while i <= n:
        if n % i == 0:
            n = n//i
            arr.append(i)
            break
        i+=1
for i in arr:
    print(i)      