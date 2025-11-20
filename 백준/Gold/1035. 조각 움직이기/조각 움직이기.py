import itertools
from collections import deque

def is_link(nodes):
    s = set(nodes)
    q = deque([nodes[0]])
    visited = {nodes[0]}

    moves = [1,-1,5,-5]

    while q:
        cur = q.popleft()
        for mv in moves:
            nxt = cur + mv
            if nxt < 0 or nxt > 24:
                continue
            if (cur % 5 == 4 and mv == 1) or (cur % 5 == 0 and mv == -1):
                continue
            if nxt in s and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
            
    return len(visited) == len(nodes)

def combo(n):
    com = []
    for i in itertools.combinations(range(25),n):
        #연결되어 있는지 확인
        #상하좌우 좌우 1차이 혹은 상하 5차이
        if is_link(i):
            com.append(i)
    return com

def dist(a,b):
    ax,ay = divmod(a,5)
    bx,by = divmod(b,5)
    return abs(ax-bx) + abs(ay-by)

def move(pieces,combs):
    k = len(pieces)
    ans = float("inf")
    for pattern in combs:
        for perm in itertools.permutations(range(k)):
            s = 0
            for i in range(k):
                s+=dist(pieces[i],pattern[perm[i]])
            if s < ans:
                ans = s
    return ans

piece = []
for i in range(5):
    line = input()
    for j in range(5):
        if line[j] == "*":
            piece.append(i*5+j) #좌표 받기

n = len(piece)
comb = combo(n)

print(move(piece,comb))