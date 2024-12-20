new_arr = []
for i in range(9):
    new_arr.append(int(input()))
print(max(new_arr))
print(new_arr.index(max(new_arr))+1)