n = int(input())
empty = n-1
for i in range(1,2*n,2):
    print(' '*empty+'*'*i)
    empty -=1
empty =1
for i in range(2*n-3,0,-2):
    print(' '*empty+'*'*i)
    empty +=1