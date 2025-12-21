'''
isdigit() - str 이 전체 숫자로 되어 있는지 검사해줌. 하나라도 문자면 false
'''
def solution(s):
    return (len(s)==4 or len(s)==6) and s.isdigit()