import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

plus, minus, multiple, div = map(int,input().split())

b = []

def dfs(deep, all_num):
    global max_, min_, plus,minus,multiple,div,b
    if deep == n:
        b.append(int(all_num))
        return
    
    if plus > 0:
        plus -= 1
        a = all_num + arr[deep]
        dfs(deep + 1,a)
        plus += 1

    if minus > 0:
        minus -= 1
        a = all_num - arr[deep]
        dfs(deep + 1,a)
        minus += 1

    if multiple > 0:
        multiple -= 1
        a = all_num * arr[deep]
        dfs(deep + 1,a)
        multiple += 1

    if div > 0:
        div -= 1
        if all_num < 0:
            a = -(abs(all_num) // arr[deep])
        else:
            a = all_num // arr[deep]
        dfs(deep + 1,a)
        div += 1

dfs(1,arr[0])
print(max(b))
print(min(b))