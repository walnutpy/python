import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s = input().rstrip()
    f = s[0]
    l = s[len(s)-1]
    print(f"{f}{l}")