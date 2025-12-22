'''
아이디어 : 유클리드 호제법 
- 최대공약수는 둘 중 작은 수와, 결국 나누고 나누다가 남는 나머지와의 작은수가 됨
+ 최소공배는 n,m 곱하면 최대공약수 두번 들어가니까 그거 한번 나누면 됨
'''
def solution(n, m):
    a, b = n, m
    while b!=0: #b 가 무조건 작아지게 만듦
        a, b = b, a%b
    
    gongyak = a
    gongbae = n*m//gongyak
    
    return [gongyak, gongbae]
        