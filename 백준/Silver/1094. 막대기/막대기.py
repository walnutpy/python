
goal = int(input())
mine = 64
length = []

length.append(mine)

def len_sum(arr):
    return sum(arr)

def count(arr):
    count = 0
    for i in arr:
        count += 1
    return count

while len_sum(length) != goal:
    length.sort()
    smallest = length.pop(0)
    a = int(smallest / 2)

    length.append(a)

    if len_sum(length) < goal:
        length.append(a)
    
print(count(length))