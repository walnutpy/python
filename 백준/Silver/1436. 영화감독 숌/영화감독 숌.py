import sys
input = sys.stdin.readline
n = int(input())
count = 0
target = '666'
num = 0
while True:
    str_num = str(num)
    if target in str_num:
        count +=1
    if count == n:
        print(num)
        break
    num+=1
