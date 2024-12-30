n = int(input())

f = 1


for i in range(1,n+1):
    f = f * i

f = str(f)

stack = 0
for i in reversed(f):
    if i == '0':
        stack += 1

    else:
        break

print(stack)