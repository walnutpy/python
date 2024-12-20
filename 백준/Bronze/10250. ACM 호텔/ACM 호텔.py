test = int(input())
for i in range(test):
    h, w, n = map(int,input().split())
    new = []
    for wide in range(1,w+1):
        for floor in range(1,h+1):
            stack = floor * 100 + wide
            new.append(stack)
    print(new[n-1])