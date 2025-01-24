w_p = [["W" for _ in range(100)]for _ in range(100)]
w_count = 10000
n = int(input())
for _ in range(n):
    l, a = map(int,input().split())
    for i in range(10):
        for j in range(10):
            row = 99 - a -i
            col = j+l -1
            if w_p[row][col] == "W":
                w_p[row][col] = "B"
                w_count -= 1
print(10000 - w_count)