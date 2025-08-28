n = int(input())
p = list(map(int,input().split()))
c = [[]for _ in range(n)]
delet = int(input())

root = -1

for i,p in enumerate(p):
    if p == -1:
        root = i

    else:
        c[p].append(i)

cnt = 0

def dfs(node):
    global cnt
    if node == delet:
        return
    if not c[node]:
        cnt += 1
        return
    
    leaf = True
    for ch in c[node]:
        if ch != delet:
            leaf = False
            dfs(ch)

    if leaf:
        cnt +=1

#자기가 del이면 안됨
#노드에 들어간거 하나씩 돌아댕김
#delete면 리턴
#이어진 노드가 비어있다면 자기가 리프가 됨
#자식이 삭제 된다면 자기 자신이 리프가 됨



if root != delet:
    dfs(root)
print(cnt)