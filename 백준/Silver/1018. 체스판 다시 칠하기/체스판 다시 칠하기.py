import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # n 세로 m 가로로

con = []

wht = [['W','B','W','B','W','B','W','B'],
       ['B','W','B','W','B','W','B','W'],
       ['W','B','W','B','W','B','W','B'],
       ['B','W','B','W','B','W','B','W'],
       ['W','B','W','B','W','B','W','B'],
       ['B','W','B','W','B','W','B','W'],
       ['W','B','W','B','W','B','W','B'],
       ['B','W','B','W','B','W','B','W']]

blk = [['B','W','B','W','B','W','B','W'],
       ['W','B','W','B','W','B','W','B'],
       ['B','W','B','W','B','W','B','W'],
       ['W','B','W','B','W','B','W','B'],
       ['B','W','B','W','B','W','B','W'],
       ['W','B','W','B','W','B','W','B'],
       ['B','W','B','W','B','W','B','W'],
       ['W','B','W','B','W','B','W','B']]

def changes(n,m,case):
    stack = 0
    for i in range(8):
        for j in range(8):
            if con[n+i][m+j] != case[i][j]:
                stack +=1
    return stack


for _ in range(n):
    line = list(input().strip())
    con.append(line)

mini = float('inf')
for i in range(n - 7):
    for j in range(m - 7):          
        W = changes(i,j,wht)
        B = changes(i,j,blk)
        mini = min(mini, W, B)

print(mini)