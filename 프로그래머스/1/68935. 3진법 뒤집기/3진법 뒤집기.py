'''
3진법 + 뒤집어진 상태로 -> %3 누적후 str
'''
def solution(n):
    base = ''
    while n:
        base += str(n%3)
        n//=3
    return int(base,3) #문자열 base 를 3진수로 해석해 10진수로 바꾸라는 것