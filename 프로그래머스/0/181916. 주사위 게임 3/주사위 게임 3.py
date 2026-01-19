from collections import Counter
'''
딕셔너리 형태로 각 숫자 몇개씩 있는지 반환하는게 Counter
'''
def solution(a, b, c, d):
    dice = [a,b,c,d]
    count = Counter(dice)
    if a == b == c == d:
        return 1111*a
    
    for num in count:
        if count[num] == 3:
            p = num #3인 값이 나온 숫자
            q = [i for i in count if count[i]==1][0]
            return (10*p + q)**2
        
    if len(count) == 2:
        if all(cnt == 2 for cnt in count.values()):
            p,q = list(count.keys()) #이렇게 만들면 반환됨
            return (p+q)*abs(p-q) #abs : 절댓값
    if len(count) == 3:
        for num in count:
            if count[num] == 2:
                others = [n for n in count if count[n]==1]
                p,q = others[0], others[1]
                return p*q
            
    return min(dice)