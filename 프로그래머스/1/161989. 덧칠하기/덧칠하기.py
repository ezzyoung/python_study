def solution(n, m, section):
    count = 0 #페인트 칠한 횟수
    paintend = 0 #현재까지 칠해진 마지막 구역 번호
    
    for s in section:
        if s>paintend:
            count +=1 #페인트 칠하는 부분 누적
            paintend = s+m -1 
    return count