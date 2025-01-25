import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = [[0 for _ in range(n)]for _ in range(n)]

apple_cnt = int(input())
for _ in range(apple_cnt):
    i,j= map(int,input().split())
    board[i-1][j-1] = 1

move = int(input())
move_arr = []
for _ in range(move):
    x, c = input().split()
    move_arr.append((int(x),c))

s_p = deque([(0,0)])
s_s = set([(0,0)])
move_i = [0,1,0,-1]
move_j = [1,0,-1,0]
time = 0
direct = 0

while True:
        time+=1
        head_i, head_j = s_p[0]
        snake_pos_i = head_i + move_i[direct]
        snake_pos_j = head_j + move_j[direct]

        if not(0<=snake_pos_i < n and 0<= snake_pos_j < n) or (snake_pos_i,snake_pos_j) in s_s:
            break

        if  board[snake_pos_i][snake_pos_j] == 1:
            board[snake_pos_i][snake_pos_j] = 0
        else:
            tail_i, tail_j = s_p.pop()
            s_s.remove((tail_i,tail_j))

        s_p.appendleft((snake_pos_i,snake_pos_j))
        s_s.add((snake_pos_i,snake_pos_j))

        if move_arr and move_arr[0][0] == time:
            if move_arr[0][1] == "D":
                direct =(direct +1) % 4
            else:
                direct =(direct -1) % 4
            move_arr.pop(0)
print(time)