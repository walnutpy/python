S = str(input())

new = ''

for i in range(97, 123):
    a = S.find(chr(i))
    new += str(a) +" "

print(new)