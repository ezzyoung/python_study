#자리수 상관없이 정수를 str 바꾸면 for i in x 가 가능해짐 (iterable)
def solution(age):
    table = 'abcdefghij'
    return ''.join(table[int(i)] for i in str(age))