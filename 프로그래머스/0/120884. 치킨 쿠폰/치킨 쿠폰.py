def solution(chicken):
    result = 0 #초기화
    coupons = chicken
    
    while coupons >= 10:
        new = coupons//10
        result += new #쿠폰수 누적
        coupons = coupons%10 + new
    return result