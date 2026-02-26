#해시 테이블 및 해시맵 사용
#key->value 저장해서 꺼내쓰고, 키값을 빠르게 찾는 자료구조

def solution(name, yearning, photo):
    #zip 함수의 경우 만약 길이가 다르면 짧은 쪽에 맞춰서 반환한다
    result = []
    #name 과 yearning 을 묶어주고 -> 이를 기반으로 photo 를 돌면서 계산한다
    score = {x:y for x, y in zip(name, yearning)} #지정해줘서 돌게 만들기
    
    for p in photo:
        total = 0
        for person in p:
            total += score.get(person,0) #해당 키에 매핑된 밸류를 가져오는것
        result.append(total) #다 돌고 append 해야 하니까
        
    return result
        