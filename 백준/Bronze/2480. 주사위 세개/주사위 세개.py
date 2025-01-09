num = list(map(int, input().split()))

count = [0] * 7
for i in num:
    count[i] += 1

money = 0

for i in range(1,7):
    if count[i] == 3:
        money = 10000 + i * 1000
        break
    elif count[i] == 2:
        money = 1000 + i * 100
        break
if money == 0:
    money = max(num) * 100 

print(money)