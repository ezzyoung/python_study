'''
무엇을 판별할 것이냐 순서
일단 나눠지나 -> 소수인가 -> 반환
true false 사용 가능성
'''
def solution(n):
    ans = []
    for i in range(2,n+1): #1미포함
        if n%i == 0:
            p=True
            for k in range(2,i):
                if i%k == 0:
                    p=False
                    break #그만 보기
            if p==True:
                ans.append(i)
    return ans
                
        
    