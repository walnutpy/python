import sys
input = sys.stdin.readline

n = int(input())

score = list(map(int, input().split()))

maxmum = max(score)
new_score = 0

for i in score:
    new_score += (i / maxmum) * 100

mid = new_score / n

print(mid)