n = int(input())

num = list(map(int, input().split()))

if n != len(num):
    exit()

count = 0

def is_prime(n):
    if n < 2:
        return False
    
    if n == 3 or n == 2:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        
        i += 6
    return True


for i in num:
    if is_prime(i):
        count +=1

print(count)