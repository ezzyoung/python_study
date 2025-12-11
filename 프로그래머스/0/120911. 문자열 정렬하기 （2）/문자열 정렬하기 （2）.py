#문자열을 list 씌우면 다 띄어서 리스트로 저장된다
def solution(my_string):
    my_string = my_string.lower()
    mystring = list(my_string)
    mystring.sort()
    return ''.join(i for i in mystring)
    