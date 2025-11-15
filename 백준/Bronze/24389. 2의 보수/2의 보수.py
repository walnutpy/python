n = int(input())
x = n&0xffffffff
y = (-n)&0xffffffff
diff = x^y
print(bin(diff).count("1"))