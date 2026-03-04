import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split())) 
S = list(map(int,input().split())) 


deck = list(range(N)) 
origin = deck[:]
cnt = 0

def is_ok(deck):
    for pos, card in enumerate(deck):
        if P[card] != pos % 3:
            return False
    return True

while True:
    if is_ok(deck):
        print(cnt)
        break
    
    nxt = [0] * N
    for i in range(N):
        nxt[S[i]] = deck[i]
    deck = nxt
    cnt += 1
    
    if origin == deck:
        print(-1)
        break