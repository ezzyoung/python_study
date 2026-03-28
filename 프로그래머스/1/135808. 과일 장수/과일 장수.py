def solution(k, m, score):
    score.sort(reverse=True) #큰 숫자부터 작은 숫자
    answer = 0
    
    for i in range(m-1, len(score), m):
        answer+=score[i]*m
        
    return answer
        