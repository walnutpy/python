import sys
input = sys.stdin.readline
s = input()
count=0
past = None
for i in s:
    if i != past:
        if past != None:
            count +=1
        past = i
if count % 2 == 0:
    print(int(count / 2))
else:
    print(int((count-1)/ 2))