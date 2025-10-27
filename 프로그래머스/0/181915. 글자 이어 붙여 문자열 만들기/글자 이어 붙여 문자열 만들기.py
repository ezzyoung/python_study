def solution(my_string, index_list):
    answer = ''.join(my_string[i] for i in index_list) #인덱스 리턴
    return answer