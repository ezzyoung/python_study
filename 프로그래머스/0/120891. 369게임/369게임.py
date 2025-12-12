def solution(order):
    sum = 0
    for i in str(order):
        if i in '369':
            sum+=1
    return sum