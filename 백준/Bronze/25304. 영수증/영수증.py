total = int(input())
n = int(input())
buy = 0
for _ in range(n):
    price , num = map(int, input().split())
    buy += price * num
if total == buy:
    print("Yes")
else:
    print("No")
