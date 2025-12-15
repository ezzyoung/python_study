def solution(n):
    fact = 1
    i = 1
    while fact*(i+1) <= n:
        i+=1
        fact*=i #i 를 곱한 후 그걸 fact 에 저장
    return i