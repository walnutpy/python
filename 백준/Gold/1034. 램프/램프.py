M,N = map(int,input().split())#행 열
arr = []
dic = {}
for _ in range(M):
    arr.append(input())
K = int(input())

# 후보키 선정

for line in arr:
    zero = line.count("0")
    if zero <= K and (K-zero)%2 == 0:
        if line in dic:
            dic[line] += 1
        else:
            dic[line] = 1

max_val = 0

for i in dic.values():
    if max_val < i:
        max_val = i

print(max_val)