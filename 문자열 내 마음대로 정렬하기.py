def solution(strings, n):
    
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    for j in strings:
        answer.append(j[1:])

    return answer

solution(["abce", "abcd", "cdx"], 2)