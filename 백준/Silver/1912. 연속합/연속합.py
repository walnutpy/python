import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

current_sum = arr[0]
max_sum = arr[0]

for i in range(1,n):
    current_sum = max(arr[i],arr[i]+current_sum)
    max_sum = max(current_sum,max_sum)
print(max_sum)


#시간 복잡도가 2중 배열이라 높아서 실패함
'''
def sum_arr(arr):
    n = len(arr)
    plus = -sys.maxsize - 1
    for i in range(n):
        for j in range(i):
            plus = max(plus,sum(arr[j:i]))
    return plus

print(sum_arr(arr))
'''
