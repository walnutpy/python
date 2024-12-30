n = int(input())

people = []

for i in range(n):
    age , name = map(str, input().split())
    age = int(age)
    people.append((age, name))

people.sort(key= lambda x : x[0])

for i in people:
    print(i[0], i[1])
