import sys

input = sys.stdin.readline

n = int(input())

con = []

for i in range(n):
    x, y = map(int, input().split())
    con.append((x,y))

con.sort(key = lambda x: (x[0], x[1]))

for i in con:
    print(i[0],i[1])