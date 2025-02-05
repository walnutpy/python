a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
#n은 n0보다 큰 수수
#fn = a1*n+a0
#gn = c * n
if a1*n0 + a0 <= c*n0 and a1 <= c:
    print(1)
else:
    print(0)