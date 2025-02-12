import sys
input = sys.stdin.readline
n = int(input().rstrip())
base_card = list(map(int,input().split()))
m = int(input())
having_card = list(map(int,input().split()))
base_card.sort()

def search(card):
    left = 0
    right = n-1
    while True:
        mid = (right+left)//2
        if card < base_card[mid]:
            right = mid - 1
        elif card == base_card[mid]:
            count = 0
            for i in range(mid,right+1):
                if base_card[i] != card:
                    break
                count+=1
            for i in range(mid-1,left-1,-1):
                if base_card[i] != card:
                    break
                count+=1
            return count
        else:
            left = mid +1

dic = {}
for i in base_card:
    if i not in dic:
        dic[i] = search(i)

arr = []

for i in having_card:
    if i in dic:
        arr.append(dic[i])
    else:
        arr.append(0)

print(*arr)