import sys
input = sys.stdin.readline
n,m = map(int,input().split())
know = set(input().split()[1:])
party = []
for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for i in party:
        if i & know:
            know = know.union(i)

count = 0

for i in party:
    if i & know:
        continue
    count += 1

print(count)