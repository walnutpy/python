n = int(input())
m = int(input())
if m != 0:
    arr = list(map(int,input().split()))
else:
    arr=[]

cnt = abs(n-100)

for i in range(1000000):
    s = str(i)
    is_ok = True
    for x in s:
        if int(x) in arr:
            is_ok = False
            break
    if is_ok:
        cnt = min(cnt,len(s)+abs(n-i))
        
print(cnt)