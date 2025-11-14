n, m = map(int,input().split())
cnt = 0
for i in range(n):
    ok = input()
    if ok.count("O") > m//2:
        cnt+=1
print(cnt)