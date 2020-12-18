def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(1, len(prices)):
        count = 0
        current = prices[i-1]
        for j in range(i, len(prices)):
            comp = prices[j]
            count += 1
            if current > comp:
                break
        answer[i-1] = count
    return answer 

prices = [1, 2, 3, 2, 3]

print(solution(prices))