def solution(progresses, speeds):
    days = 1
    answer = []
    count = 0
    while len(progresses) > 0:
        if(progresses[0] + (days * speeds[0])) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1
        
    answer.append(count)
    return answer
progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))