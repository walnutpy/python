y  = input()
pront = int(y[0:2])
back = int(y[2:4])
while True:
    if y == "9999":
        print(-1)
        break
    back += 1
    if back > 99 or pront > 99:
        back = 0
        pront += 1
    if pront == 99 and back == 99:
        print(-1)
        break
    if (pront + back)**2 == 100*pront + back:
        print(100*pront + back)
        break