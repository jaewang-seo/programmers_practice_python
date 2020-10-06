# import itertools
# def solution(clothes):
#         answer = 0
#         clo_dict = {}
#         count = 0
#         for a, b in clothes:
#             clo_dict.setdefault(a, b)
#         count = len(clo_dict.keys())
#         a = list(clo_dict.values())
        
#         b = list(itertools.combinations(a, 2))
#         count += b
#         c = clo_dict.values()
#         d = set(c)
#         print("OK")

#     return answer

def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: 
            answer[i[1]] += 1
        else: 
            answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1

# de_di = {}
# a = "hii"
# de_di[a] = 1

# print("OK")
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
