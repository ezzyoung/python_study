def solution(myString):
    return sorted([i for i in myString.split('x') if i!='']) #sorted 은 반환되나 오리지널 안건들임 sort 는 반환 안되고 오리지널 건드림