n = int(input())
count = 1
plus = 0
while n > plus:
    plus = (count)*(count+1) // 2
    count += 1
count -=1
n -= ((count-1)*(count)) // 2
if count % 2 == 0:
    a = count - n +1
    b = n
else:
    a = n
    b = count - n +1
print(f"{b}/{a}")