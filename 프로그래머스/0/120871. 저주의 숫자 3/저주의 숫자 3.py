def solution(n):
    count = 0
    x =0 #전부 초기화
    
    while count<n:
        x+=1
        if x%3!=0 and '3'not in str(x):
            count+=1 #실제수
    return x
    