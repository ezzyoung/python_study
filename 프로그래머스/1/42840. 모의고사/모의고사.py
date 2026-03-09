#완전탐색
def solution(answers):
    su1 = [1,2,3,4,5]
    su2 = [2,1,2,3,2,4,2,5]
    su3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0,0,0] #점수기록 리스트
    
    for i, ens in enumerate(answers): #인덱스와 값
        if ens == su1[i%len(su1)]:
            scores[0] += 1
        if ens == su2[i%len(su2)]:
            scores[1] += 1
        if ens == su3[i%len(su3)]:
            scores[2] += 1
    
    maxscore = max(scores) #최대값 추출
    
    return [i+1 for i, s in enumerate(scores) if s==maxscore]
        