import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemon = {}

for i in range(n):
    name = input().strip()
    pokemon[i+1] = name
    pokemon[name] = i+1

for _ in range(m):
    question = input().strip()
    if question.isdigit():
        print(pokemon[int(question)])
    else:
        print(pokemon[question])