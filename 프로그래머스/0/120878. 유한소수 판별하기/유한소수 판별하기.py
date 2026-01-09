import math
def solution(a, b):
    g = math.gcd(a,b)
    b//=g #b 를 최대공약수로 나눈 값 b 에 저장
    while b%2 ==0:
        b//=2
        
    while b%5 ==0:
        b//=5
    return 1 if b ==1 else 2
    