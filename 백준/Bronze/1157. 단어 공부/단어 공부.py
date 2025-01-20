s=input().upper()
dic = dict()
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1

max_val = max(dic.values())
max_key = [key for key, val in dic.items() if val == max_val]
if len(max_key) > 1:
    print('?')
else:
    print(*max_key)