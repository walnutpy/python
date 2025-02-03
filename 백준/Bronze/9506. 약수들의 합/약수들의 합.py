def factor(n):
    arr = []
    i = 1
    while i < n:
        if n % i ==0:
            arr.append(i)
        i +=1
    if sum(arr) == n:
        return arr
    else:
        return 0
while True:
    n = int(input())
    if n == -1:
        break
    arr = factor(n)
    if arr == 0:
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} ="," + ".join(map(str,arr)))