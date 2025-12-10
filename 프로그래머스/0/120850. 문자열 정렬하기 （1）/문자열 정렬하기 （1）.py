#isdigit() - 특정 문자가 숫자인지 아닌지 판별해준다고 함. i.isdigit() 하면 됨 (숫자 판별)
def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])
    