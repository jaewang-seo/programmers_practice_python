def solution(answers):
    answer = []
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == man1[i % len(man1)]:
            count[0] += 1
        if answers[i] == man2[i % len(man2)]:
            count[1] += 1
        if answers[i] == man3[i % len(man3)]:
            count[2] += 1    
    
    max_score = max(count)
    for i in range(3):
        if count[i] == max_score:
            answer.append(i+1)            
    return answer