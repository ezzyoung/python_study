def solution(arr, k):
    if k %2 ==1:
        arr = [a*k for a in arr] #리스트에 적용시켜주려면 명시적으로 표시
    else:
        arr = [a+k for a in arr]
    return arr