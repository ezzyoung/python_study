def solution(before, after):#sort 는 오로지 리스트용 sorted 는 문자열에도 사용 가능
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0