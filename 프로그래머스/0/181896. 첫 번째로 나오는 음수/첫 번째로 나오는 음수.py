def solution(num_list):
    for i, v in enumerate(num_list): #리스트에서 순차적으로 도는 함수
        if v < 0:
            return i
    return -1
