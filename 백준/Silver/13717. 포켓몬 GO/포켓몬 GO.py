n = int(input())
cnt = 0
max_ev = 0
good = ""
for i in range(n):
    name = input()
    k, m = map(int,input().split())
    count = 0
    while m >= k:
        m -= k
        m+=2
        count += 1
        cnt += 1
    if count > max_ev:
        good = name
        max_ev = count
print(cnt)
print(good)