from collections import deque


def bfs(n,k):
    visited = {(n,0)}
    q = deque()
    q.append((n,0))
    ans = -1
    m = len(n)

    while q:
        num, cnt = q.popleft()
        if cnt == k:
            ans = max(ans,int(num))
            continue
        for i in range(m-1):
            for j in range(i+1,m):
                if i == 0 and num[j] == '0':
                    continue
                lst = list(num)#문자열은 교환이 안됨
                lst[i],lst[j]=lst[j],lst[i]
                nxt = ''.join(lst)#다시 합쳐주기
                if (nxt,cnt+1) not in visited:
                    visited.add((nxt,cnt+1))
                    q.append((nxt,cnt+1))
    return ans 

n,k = map(int,input().split())
n = str(n)

print(bfs(n,k))