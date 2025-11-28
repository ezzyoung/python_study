def solution(num_list):
    cnt=0 #count 초기화
    for i in num_list:
        while i!=1: #i가 1이 아닐때까지
            if i%2==0:
                i=i//2
                cnt+=1
            elif i%2==1:
                i=(i-1)//2
                cnt+=1
    return cnt #return 위치 잘 생각할게, 전체 다 돌고 반환하게 하기
        