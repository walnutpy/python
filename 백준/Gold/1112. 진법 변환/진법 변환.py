x, b = map(int, input().split())
num = ''

if x == 0:
    num = '0'

negative = False
if x < 0 and b > 0:
    x *= -1
    negative = True

while x != 0:
    q, r = divmod(x, b)
    if r < 0:
        q += 1
        r -= b
    num = str(r) + num
    x = q 

if negative:
    print(-1 * int(num))
else:
    print(int(num))