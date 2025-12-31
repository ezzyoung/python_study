'''
튜플 앞에서부터 저장 이유 - sort 시 자동으로 앞에서부터 비교함
'''
def solution(rank, attendance):
    result = []
    for i, (r,ok) in enumerate(zip(rank, attendance)): #zip 이 묶어 생각
        if ok:
            result.append((r,i)) #rank 와 번호
    result.sort()
    
    a = result[0][1]
    b = result[1][1]
    c = result[2][1]
    
    return 10000*a + 100*b + c
            