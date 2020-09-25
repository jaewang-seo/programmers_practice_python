def solution(array, commands):
    
    # array의 결과를 저장할 리스트
    answer = []

    # 최종 결과를 저장할 리스트 
    re_result = []

    # commands에서 1차원 배열 가져오기
    for i in commands:

        # 1차원 배열의 순서태로의 값을 이용해 array에서 가져온다
        answer = sorted(array[i[0]-1:i[1]])

        # answer에서 i[2]-1 번째의 값을 가져옴
        re_result.append(answer[i[2]-1])

    return re_result


