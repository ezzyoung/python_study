'''
리스트의 max 값도 구할 수 있다
'''
def solution(array):
    return [max(array),array.index(max(array))] #배열.index(찾을값) 