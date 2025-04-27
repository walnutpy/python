n,m = map(int,input().split())
#소시지 n 사람 m
def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
"""
3 7

1111 1111 1111

4 = (7 - 3) = (m-n)
칼질 3회

1 1 1
1 = (4 -3) = (m-n-n)
칼질 6회


"""

print(m - gcd(n,m))