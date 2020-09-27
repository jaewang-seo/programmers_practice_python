def solution(a, b):

    sum_result = []
    answer = 0
    if a <= b:
        for i in range(a, b+1):
            sum_result.append(i)
        answer = sum(sum_result)
    else:
        for i in range(b, a+1):
            sum_result.append(i)
        answer = sum(sum_result)
    print("OK")
        

    return answer

solution(3, 3)