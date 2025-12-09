def solution(num, k):
    numbers = list(str(num)) #str 만든 후 숫자 일일히 분리하려면 list 화
    k = str(k)
    if k in numbers:
        return numbers.index(k)+1
    else:
        return -1