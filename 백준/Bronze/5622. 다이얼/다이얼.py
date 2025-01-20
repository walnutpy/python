import sys
input = sys.stdin.readline
s = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for i in s:
    for j in dial:
        if i in j:
            time += dial.index(j)+3
print(time)