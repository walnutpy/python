case_OX = int(input())

quiz = []

for i in range(case_OX):
    sol = input()
    quiz.append(sol)

target = "O"



for i in range(case_OX):
    score = 0
    stack = 0

    for a in quiz[i]:
        if a == target:
            score +=1 + stack
            stack +=1

        else:
            stack = 0

    print(score) 