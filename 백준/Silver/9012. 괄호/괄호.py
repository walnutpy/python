import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    VPS = input().rstrip()
    balance = 0
    valid = True
    for ch in VPS:
        if ch == '(':
            balance+=1
        else:
            balance-=1
        if balance < 0:
            valid = False
            break

    if balance !=0:
        valid = 0

    if valid:
        print("YES")
    else:
        print("NO")