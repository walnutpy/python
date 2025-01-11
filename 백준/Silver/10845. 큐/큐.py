from collections import deque
import sys 
input = sys.stdin.readline

n = int(input())

cases = deque()

def que(command, arr):
    match command[0]:
        case 'push':
            arr.append(command[1])
            return arr
        
        case 'pop':
            if len(arr) != 0:
                print(arr.popleft())
            else:
                print(-1)
            return arr
        
        case 'size':
            print(len(arr))
            return arr
        
        case 'empty':
            if len(arr) == 0:
                print(1)
            else:
                print(0)
            return arr
        
        case 'front':
            if len(arr) != 0:
                print(arr[0])
            else:
                print(-1)
            return arr
        
        case 'back':
            if len(arr) != 0:
                print(arr[-1])
            else:
                print(-1)
            return arr

for _ in range(n):
    c = input().strip().split()
    cases = que(c, cases)