import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().rstrip().split()))
v = int(input())
print(arr.count(v))