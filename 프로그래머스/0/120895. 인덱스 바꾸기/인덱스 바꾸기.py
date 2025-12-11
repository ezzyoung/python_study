'''
    mystring[num1] = mystring[num2]
    mystring[num2] = mystring[num1] 이렇게 하면 원본이 없어져서 안됨
'''
def solution(my_string, num1, num2):
    mystring = list(my_string)
    mystring[num1], mystring[num2] = mystring[num2], mystring[num1] #파이썬식 swap
    return ''.join(i for i in mystring)