def solution(a, d, included):
    sum = 0
    for i, value in enumerate(included):
        if value:
            sum+=a+i*d
    return sum #다 돌고 반환