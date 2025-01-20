import sys
input = sys.stdin.readline

a, b = map(str,input().rstrip().split())
a = a[::-1]
b = b[::-1]
if int(a)>int(b):
    print(a)
else:
    print(b)