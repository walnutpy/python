n , k = map(int,input().split())

n_p = 1
k_p = 1
n_k = 1

for i in range(1,n+1):
    n_p = n_p * i

for i in range(1,k+1):
    k_p = k_p * i

for i in range(1,n - k + 1):
    n_k = n_k * i

result = int(n_p / (k_p * n_k))


print(result)