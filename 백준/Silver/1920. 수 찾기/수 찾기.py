import sys
input = sys.stdin.readline

n = int(input())

case = list(map(int, input().split()))

m = int(input())

stand = list(map(int, input().split()))

'''
count = [0] * 4294967297

for i in case:
    count[2147483649 + i] += 1


    
for i in stand:
    if count[i + 2147483649] > 0:
        stand[stand.index(i)] = 1
    else:
        stand[stand.index(i)] = 0
'''
case = set(case)

result = [1 if num in case else 0 for num in stand]

for i in result:
    print(i)