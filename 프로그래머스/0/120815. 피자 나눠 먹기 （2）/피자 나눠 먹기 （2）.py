def solution(n):
    i =1 #피자 한판부터 시작
    while True:
        if (i*6)%n == 0:
            return i #최소 i 찾고 종료
        i+=1
            
        