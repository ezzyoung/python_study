def solution(array): #아직은 중앙값 리스트에서 구할때 홀수라도 정수로 나누면 괜찮음
    array.sort()
    mid = len(array)//2
    return array[mid]
    