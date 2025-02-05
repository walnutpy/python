while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    max_num = max(a,b,c)
    if   max_num < (a+b+c-max_num):
        if a == b == c:
            print("Equilateral")
        elif a==b or b==c or c==a:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")