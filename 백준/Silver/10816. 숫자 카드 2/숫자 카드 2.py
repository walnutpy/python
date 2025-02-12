import sys
input = sys.stdin.readline
n = int(input().rstrip())
base_card = list(map(int,input().split()))
m = int(input())
having_card = list(map(int,input().split()))
dic ={}
for i in base_card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

arr = []
for i in having_card:
    if i in dic:
        arr.append(dic[i])
    else:
        arr.append(0)

print(*arr)