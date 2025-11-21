N = int(input())
arr = [0]*N
for i in range(N):
    line = input()
    for c,ch in enumerate(line):
        if ch == "T":
            arr[c] |= (1<<i)
ans = float("inf")

for i in range(1<<N):
    cnt = 0
    for c in range(N):
        zero = (arr[c]^i).bit_count()#뒷면수 세기 만약에 N이 101이면 열에 대해서 1 0 1각각 xor
        cnt += min(zero,N-zero)
    if ans > cnt:
        ans = cnt
print(ans)
