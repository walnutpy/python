import sys
input = sys.stdin.readline

def fun(com, arr):
    if len(com) > 1:
        com[1] = int(com[1])
    match com[0]:
        case 'add':
            if com[1] not in arr:
                arr.add(com[1])
            return arr
        
        case 'remove':
            if com[1] in arr:
                arr.remove(com[1])
            return arr
        
        case 'check':
            if com[1] in arr:
                print(1)
            else:
                print(0)
            # print(1 if com[1] in arr else 0)
            return arr
        
        case 'toggle':
            if com[1] not in arr:
                arr.add(com[1])
            else:
                arr.remove(com[1])
            return arr
        
        case 'all':
            arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
            return arr
        
        case 'empty':
            arr = set()
            return arr

n = int(input())
num = set()

for _ in range(n):
    com = input().strip().split()
    num = fun(com, num)