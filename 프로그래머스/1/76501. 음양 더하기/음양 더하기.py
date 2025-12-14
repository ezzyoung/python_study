def solution(absolutes, signs):
    answer = 0
    for a, j in zip(absolutes, signs): #나누는 법 zip 으로
        if j:
            answer+=a
        else:
            answer-=a
    return answer
        
    
                