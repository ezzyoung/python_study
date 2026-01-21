'''
고정 형태의 경우 zip 쓰는 방법이 수월할수도
아이디어 - 선분 개수라고 해봤자 가지수는 3개
0,1,2,3 인덱스 있을때
0,1 // 2,3
0,2 // 1,3
0.3 // 2,4
'''
def solution(dots):
    def parellel(a,b,c,d): #dots 내에 인덱스를 주는 방법으로
        x1, y1 = dots[a]
        x2, y2 = dots[b]
        x3, y3 = dots[c]
        x4, y4 = dots[d]
        
        return (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1)
    if parellel(0,1,2,3):
        return 1
    elif parellel(0,2,1,3):
        return 1
    elif parellel(0,3,1,2):
        return 1
    else:
        return 0
        