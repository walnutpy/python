import re

T = int(input())

pattern = r"(100+1+|01)+"

for _ in range(T):
    s = input()
    if re.fullmatch(pattern,s):
        print("YES")
    else:
        print("NO")