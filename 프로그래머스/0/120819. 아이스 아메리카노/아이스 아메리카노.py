def solution(money):
    answer = []
    answer.append(int(money / 5500))
    answer.append(money - (money // 5500 * 5500))  
    return answer