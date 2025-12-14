'''
lambda 매개변수들 : 반환값
'''
def solution(array, n):
    return min(array, key=lambda x: (abs(x-n),x)) #튜플 - 양값 같이 비교