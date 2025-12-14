'''
순위 자체가 인덱스
'''
def solution(emergency):
    em = sorted(emergency, reverse=True)
    return [em.index(i)+1 for i in emergency] #원래거 보존해서 인덱스 추출 but 순위는 em 으로