def solution(balls, share):
    a,b = 1, 1
    for i in range(1, share+1):#share 까지 돌기
        a*=balls
        balls-=1 #하나씩 줄여가는 펙토리얼
        b*=i #share 펙토리얼
    return int(a/b)
        
    