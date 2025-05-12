while True:
    n = input()

    if n == '0':
        break

    l = len(n) - 1
    is_pel = True

    for i in range(l//2+1):
        if n[i] != n[l-i]:
            is_pel = False
            break

    if is_pel:
        print("yes")
    else:
        print("no")