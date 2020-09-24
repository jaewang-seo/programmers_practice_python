from itertools import combinations

def solution(numbers):
    
    answer = set()
    for i in list(combinations(numbers, 2)):
        # a.append(i)
        answer.add(sum(i))
        
    return sorted(answer)