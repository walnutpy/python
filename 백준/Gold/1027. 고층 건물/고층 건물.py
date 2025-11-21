# N buildings
# A에서 B를 보려면 그 사이에 더 높은 빌딩이 없어야됨
#두 건물을 이었을 때 그래프가 나오는데 거기에 다른 점이 위에 있거나
#점하면 안됨
# 2 5 7 -> 0 3 5

# 각점과의 기울기 다 구하고 기울기 비교해서 기울기가 더 크면 보임
N = int(input())
arr = list(map(int,input().split()))
lin = [[0]*N for _ in range(N)]

#기울기 구하기
for i in range(N):
    for j in range(i+1,N):
            lin[i][j] = (arr[j]-arr[i])/(j-i)
            lin[j][i] = lin[i][j]
#기울기 비교하기
#A B의 기울기 사이에 있는 점과 A와의 기울기 비교
#만약 비교한 기울기가 더 작다면 보임 작지 않으면 보이지 않음

def right(n,r_l):
    #오른쪽
    cnt = 0
    for j in range(n+2,N):
        if r_l < lin[n][j]:
            r_l = lin[n][j]
            cnt += 1
    return cnt

def left(n,l_l):
    cnt = 0
    for j in range(n-2,-1,-1):
        if l_l > lin[n][j]:
            l_l = lin[n][j]
            cnt += 1
    return cnt

see = []
for i in range(N):
    r = 0
    l = 0

    if i != N-1:
        r_l = lin[i][i+1]
        r += 1
        r += right(i,r_l)
    else:
        r_l = 0
    
    if i != 0:
        l_l = lin[i][i-1]
        l += 1
        l += left(i,l_l)
    else:
        l_l=0
    see.append(l+r)
print(max(see))