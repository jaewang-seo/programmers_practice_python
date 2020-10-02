def solution(s):

    answer = True
    if len(s) == 6 or len(s) == 4:
            try:
                int(s)
            except ValueError:

                answer = False
            else:
                answer = True
    else:
        answer = False
    return answer

# b = a % 1

solution("1234")