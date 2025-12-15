'''
sorted 해서 반환, 아니면 0
'''
def solution(arr, divisor):
    answer = sorted([i for i in arr if i%divisor == 0])
    return answer if answer else [-1]