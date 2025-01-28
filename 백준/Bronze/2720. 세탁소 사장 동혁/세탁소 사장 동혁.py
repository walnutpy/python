import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    money = [25, 10, 5, 1]
    c = int(input())
    m_b = []
    for i in money:
        a = c // i
        m_b.append(int(a))
        c -= a * i
    print(*m_b)