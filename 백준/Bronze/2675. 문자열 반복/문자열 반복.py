T = int(input())
every = []

for i in range(0, T):
    R, S = map(str, input().split())
    R = int(R)
    type_ = []
    type_.append(R)
    type_.append(S)
    every.append(type_)

for b in range(0, T):
    answer=''
    for a in every[b][1]:
        answer += a * every[b][0]
    print(answer)