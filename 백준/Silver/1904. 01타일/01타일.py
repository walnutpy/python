n = int(input())
if n == 1:
    print(1)
else:
    a,b=1,2
    for _ in range(3,n+1):
        a,b = b, (a+b)%15746
    print(b)