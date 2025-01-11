import sys
input = sys.stdin.readline

def fun(a, b):
    gcd = min(a, b)
    while True:
        if a % gcd == 0 and b % gcd == 0:
            lcm = int((a * b) / gcd)
            print(gcd)
            print(lcm)
            return gcd, lcm
        gcd = gcd - 1


a, b = map(int, input().split())
fun(a,b)