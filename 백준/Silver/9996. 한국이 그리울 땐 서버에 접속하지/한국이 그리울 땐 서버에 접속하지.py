
import sys
input = sys.stdin.readline

n = int(input())

pattern = input().rstrip()

front = ""
back = ""
is_star = False

for i in pattern:
    if i =="*":
        is_star = True
        continue
    if is_star:
        back+=i
    else:
        front+=i

for _ in range(n):
    s = input().rstrip()
    if len(front)+len(back)>len(s):
        print("NE")
        continue
    if s.startswith(front) and s.endswith(back):
        print("DA")
    else:
        print("NE")