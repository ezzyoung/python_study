'''
분수끼리 덧셈을 어떻게 표현할지 아이디어
'''
import math
def solution(numer1, denom1, numer2, denom2):
    up = numer1 * denom2 + numer2*denom1
    down = denom1 * denom2
    
    #최대공약수로 약분
    gcd = math.gcd(up, down) #최대공약수 추출
    return [up//gcd, down//gcd]
    