T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print(1,0)
        continue
    if n == 1:
        print(0,1)
        continue
    if n == 2:
        print(1,1)
        continue
    a,b = 1, 1
    for i in range(n-2):
        a,b = b,a+b
    print(a, b)