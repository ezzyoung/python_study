def solution(a, b, c):
    #{} - set - 중복을 허용하지 않는다
    s1 = a + b + c
    s2 = a*a + b*b + c*c
    s3 = a*a*a + b*b*b + c*c*c
    
    uniq = len({a,b,c})
    if uniq == 1 :
        #세개다 같다
        return s1*s2*s3
    elif uniq == 2:
        return s1*s2
    elif uniq == 3:
        return s1 
    
    