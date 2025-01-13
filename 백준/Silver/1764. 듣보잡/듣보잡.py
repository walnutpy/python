import sys
input = sys.stdin.readline
n, m = map(int, input().split())

l = set()
s = set()

for i in range(n):
    person = input().strip()
    l.add(person)

for i in range(m):
    person = input().strip()
    s.add(person)

no_listen_see = sorted(l & s)

print(len(no_listen_see))
for i in no_listen_see:
    print(i)