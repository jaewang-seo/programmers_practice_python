import collections

def solution(participant, completion):
    answer = list(collections.Counter(participant) - collections.Counter(completion))
    
    return answer[0]