import sys
input = sys.stdin.readline

count = [i+1 for i in range(30)]
for _ in range(28):
    a = int(input())
    count[a-1] +=1

for i in range(30):
    if i+1 == count[i]:
        print(i+1)