def solution(left, right):
    sum1 = 0 #최종 정답 
    for i in range(left, right+1):
        cnt = 0 #약수 개수 세기 초기화
        for a in range(1,i+1):
            if i%a == 0:
                cnt+=1
                
        if cnt %2 == 0:
            sum1 += i
        else:
            sum1 -= i
            
    return sum1