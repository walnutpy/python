n = int(input())
dice = list(map(int,input().split()))

def two():
    duo = 10**9
    for i in range(6):
        for j in range(i+1,6):
            if 5 - i == j:
                continue
            duo = min(duo, dice[i]+dice[j])
    return duo

def three():
    trio = 10**9
    pairs = [(0,5),(1,4),(2,3)]
    for i in pairs[0]:
        for j in pairs[1]:
            for k in pairs[2]:
                trio = min(trio,dice[i]+dice[j]+dice[k])
    return trio

def roll():
    if n==1:
        print(sum(dice)-max(dice))
        return
    
    if n==2:
        #2
        duo = two()
        #3
        trio = three()
        print((4*duo)+(4*trio))            
        return
    
    else:
        trio = three()
        duo = two()
        one = min(dice)
        
        a = (one*(n-2)*(n-2)) + (one*(n-2)*(n-1)*4)
        b = (duo*(n-1)*4) + (duo*(n-2)*4)
        c = trio*4
        print(a+b+c)
        return
    
roll()