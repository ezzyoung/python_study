def solution(n):
    return n//7+(1 if n%7 >0 else 0) #리스트 컴프리헨션으로 쓰면 else 0 이 필요