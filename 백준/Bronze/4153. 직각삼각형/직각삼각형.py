while True:
    num = list(map(int,input().split()))

    num.sort()

    if not num[2]:
        break

    if num[0]**2 + num[1]**2 == num[2]**2:
        print("right")

    else:
        print("wrong")