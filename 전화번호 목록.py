# def solution(phone_book):
#     answer = True

#     front_list = []
#     end_list = []

#     for i in range(0, len(phone_book)-1):
        
#         if answer == True:
#             num = list(phone_book[i])
#             num2 = list(phone_book[i+1])

#             end_list = int(num[-1])
#             front_list = int(num2[0])
#             if end_list == 9 and front_list == 0:
#                 answer = True
#                 continue

#             if end_list == front_list-1:
#                 answer = True
#             else:
#                 answer = False
#                 break
#         else:
#             answer = False

#     return answer
def solution(phone_book):
    for a in range(len(phone_book)):
        k1 = len(phone_book[a])
        for b in range(a+1, len(phone_book)):
            k2 = len(phone_book[b])
            if phone_book[a] in phone_book[b][:k1] or phone_book[b] in phone_book[a][:k2]:
                return False
    return True
    
solution(["119", "07674223", "1195524421"])