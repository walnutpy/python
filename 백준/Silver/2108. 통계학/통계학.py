import sys
input = sys.stdin.readline
n = int(input().rstrip())

arr = []
for _ in range(n):
    a = int(input().rstrip())
    arr.append(a)

arr.sort()
mid = n//2

print(round(sum(arr)/n)) #산술평균

print(arr[mid]) #중앙값

dic = {}
for a in arr:
  if a not in dic:
    dic[a] = 1
  else:
    dic[a] += 1
max_cnt = max(dic.values())
max_arr = sorted([i for i, j in dic.items() if j == max_cnt])
print(max_arr[0] if len(max_arr)==1 else max_arr[1])


print(arr[-1] - arr[0])#범위