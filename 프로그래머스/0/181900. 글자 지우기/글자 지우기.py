def solution(my_string, indices):
    remove = set(indices) #해시 기반, 인덱스 기반으로 저장하는 편
    return "".join(j for i,j in enumerate(my_string) if i not in remove)