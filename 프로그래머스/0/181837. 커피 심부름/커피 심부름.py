#여러 key 가 하나의 value 가능
def solution(order):
    money = []
    menu_dict = {
    "iceamericano": "차가운 아메리카노",
    "americanoice": "차가운 아메리카노",

    "hotamericano": "따뜻한 아메리카노",
    "americanohot": "따뜻한 아메리카노",

    "icecafelatte": "차가운 카페 라테",
    "cafelatteice": "차가운 카페 라테",

    "hotcafelatte": "따뜻한 카페 라테",
    "cafelattehot": "따뜻한 카페 라테",

    "americano": "아메리카노",
    "cafelatte": "카페 라테",

    "anything": "아무거나"
}
    for i in order:
        if menu_dict[i] in (
        "차가운 아메리카노",
        "따뜻한 아메리카노",
        "아메리카노",
        "아무거나"): #set 으로 묶어서 다중은 처리
        
            money.append(4500)
        else:
            money.append(5000)
    
    return sum(money)