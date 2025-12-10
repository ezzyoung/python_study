def solution(box, n):
    a,b,c = box
    a = a//n
    b = b//n
    c = c//n
    return a*b*c