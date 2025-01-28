N, B = map(int,input().split())
arr = []
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
while N > 0:
    result = digits[N % B] + result
    N = N // B

print(result)