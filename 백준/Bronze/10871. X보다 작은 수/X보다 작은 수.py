import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
small = []
for i in arr:
    if i < x:
        small.append(i)
    
print(*small)