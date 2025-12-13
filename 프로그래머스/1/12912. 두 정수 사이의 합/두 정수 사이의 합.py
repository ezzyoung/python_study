def solution(a, b):
    total = 0
    a, b = min(a,b), max(a,b)
    for i in range(a,b+1):
        total +=i 
    return total
#그냥 바로 sum(i) 안되는 이유는 i 는 그저 정수 하나, sum 은 iterable 만 받을 수 있음