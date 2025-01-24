import sys
input = sys.stdin.readline
num=[]
for _ in range(9):
    num.append(list(map(int,input().split())))
max_point = -1
max_i = 0
max_j = 0
for i in range(9):
    for j in range(9):
        if num[i][j] > max_point:
            max_point = num[i][j]
            max_i ,max_j = i,j  
print(max_point)
print(max_i + 1,max_j+1)