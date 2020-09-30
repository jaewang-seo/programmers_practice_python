def solution(s):
    a = s.lower()
    p_count = a.count('p')
    y_count = a.count('y')

    if p_count == y_count:
        answer = True
    else:
        answer = False
        
    return answer

solution("pPoooyY")