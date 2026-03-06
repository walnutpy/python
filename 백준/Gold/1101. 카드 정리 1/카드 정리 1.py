import sys
input = sys.stdin.readline
n,m=map(int,input().split())

box = []

for i in range(n):
    box.append(list(map(int,input().split())))    

joker = [-1] + list(range(n))

def get_color(arr):
    for i, x in enumerate(arr):
        if x > 0:
            return i
    return -1

ans = 99999999999999
for j in joker:
    move = 0
    used = set()
                
    for i in range(n):
        if i==j:
            continue
        if m - box[i].count(0) >= 2:
            move += 1
        elif m - box[i].count(0) == 1:
            c = get_color(box[i])
            if c in used:
                move+=1
            else:
                used.add(c)
    ans = min(ans,move)
print(ans)