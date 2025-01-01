n = int(input())

words = []

for i in range(n):
    words.append(input())
    

sort_words = sorted(set(words), key=lambda x: (len(x), x))

for i in sort_words:
    print(i)