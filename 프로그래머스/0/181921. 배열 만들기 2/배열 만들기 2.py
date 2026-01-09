'''
all() 는 안에 있는게 전부 참일때만 true
'''
def solution(l, r):
    answer = [i for i in range(l,r+1) if all(c in '05' for c in str(i))]
    return answer if answer else [-1]