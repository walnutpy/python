import sys
input = sys.stdin.readline

D = [
    "####.##.##.####", # 0
    "..#..#..#..#..#", # 1
    "###..#####..###", # 2
    "###..####..####", # 3
    "#.##.####..#..#", # 4
    "####..###..####", # 5
    "####..####.####", # 6
    "###..#..#..#..#", # 7
    "####.#####.####", # 8
    "####.####..####"  # 9
]

# 입력 처리
n = int(input())
O = [''for _ in range(n)]
for i in range(5):
    line = input()
    for j in range(n):
        s = 4 * j
        O[j] += line[s:s+3]
        
poss = [[]for _ in range(n)]

#비교 처리
for i in range(n):
    o = O[i]
    for j in range(10):
        ok = True
        for k in range(15):
            if o[k] == '#' and D[j][k] == '.':
                ok = False
                break
        if ok:
            poss[i].append(j)

#평균 처리
evg = 0
for i in range(n):
    if not poss[i]:
        print(-1)
        exit()
    evg+=(sum(poss[i])/len(poss[i])) * (10**(n-i-1))
    
print(evg)
