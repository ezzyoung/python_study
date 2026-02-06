def solution(a, b, n):
    answer = 0
    while n>=a:
        get = (n//a)*b
        answer+=get
        n = (n%a) + get #순환구조
    return answer