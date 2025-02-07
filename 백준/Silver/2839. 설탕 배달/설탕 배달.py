n = int(input())
arr=[]
i = 0
while 3*i <= n:
    m_n = n - i*3
    if m_n % 5 == 0:
        count_5 = m_n // 5
        arr.append(count_5+i)
    i+=1
print(min(arr) if arr else -1)