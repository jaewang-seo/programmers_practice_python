def solution(s):

    answer = ''

    #짝수
    if len(s) % 2 == 0:

        a = int(len(s) / 2)
        answer += s[a-1] + s[a]

    else:

        b = int(len(s) / 2)
        answer += s[b]        

        print("OK")
    
    return answer

solution('abcde')