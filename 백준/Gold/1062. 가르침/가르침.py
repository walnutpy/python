import sys
input = sys.stdin.readline

n, k = list(map(int, input().rstrip().split()))
letters = [False] * 26
words = [list(input().rstrip()) for _ in range(n)]

for l in ['a', 'n', 't', 'i', 'c']:
    letters[ord(l) - ord('a')] = True

if k<5:
    print(0)
    exit()

if k >=26:
    print(n)
    exit()

ans = 0

def back(p,cnt):
    global ans
    if cnt == k - 5:
        temp= 0
        for word in words:
            learn = True
            for l in word:
                if not letters[ord(l) - ord('a')]:
                    learn = False
                    break
            if learn:
                temp += 1
        ans = max(ans,temp)
        return
    for i in range(p,26):
        if not letters[i]:
            letters[i] = True
            back(i,cnt + 1)
            letters[i] = False

back(0,0)
print(ans)