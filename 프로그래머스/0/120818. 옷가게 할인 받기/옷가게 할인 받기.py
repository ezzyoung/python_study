def solution(price):#할인률 관련된 문제는 누적형으로 풀자
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000:
        return int(price*0.9)
    elif price>=100000:
        return int(price*0.95)
    else:
        return price