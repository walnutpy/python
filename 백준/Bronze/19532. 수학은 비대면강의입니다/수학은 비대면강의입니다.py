a,b,c,d,e,f=map(int,input().split())
#ax+by=c
#dx+ey=f
m_b = d*b
m_c = d*c
m_e = a*e
m_f = a*f
y = (m_c-m_f)//(m_b-m_e)
if a!=d:
    x = ((c-f)-((b-e)*y))//(a-d)
else:
    x = (c - b*y) // a
print(x, y)