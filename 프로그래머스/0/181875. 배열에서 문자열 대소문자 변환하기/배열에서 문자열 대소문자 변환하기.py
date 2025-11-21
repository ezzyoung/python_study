def solution(strArr):
    return [s.lower() if i%2==0 else s.upper()
           for i,s in enumerate(strArr)] #리스트 컴프리헨션은 if 가 먼저 올 수 없다