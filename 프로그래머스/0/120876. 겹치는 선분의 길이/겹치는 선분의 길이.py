def solution(lines):
    hub = [0]*201 #범위에 따라 겹치는 정도를 숫자로 표현하기 위해 0 초기화
    for a, b in lines: #같은 형태의 배열이 저장되어 있을 경우 추출 가능
        for x in range(a,b):
            hub[x+100] +=1
    return sum(1 for h in hub if h>=2)
    