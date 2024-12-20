n = int(input())
sum_list = []

for i in range(n):
    a, b = map(int, input().split())
    sum = a + b
    sum_list.append(sum)

for i in sum_list:
    print(i)