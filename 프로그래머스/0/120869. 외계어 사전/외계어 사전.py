'''
순서에 상관없이 해당 원소가 있는지 확실한 확인이 필요하면 정렬이 좋다 (sorted)
'''
def solution(spell, dic):
    target = ''.join(sorted(spell))
    for i in dic:
        if ''.join(sorted(i)) == target: #i 를 알파벳 순서로 정렬시켜줌
            return 1
    return 2 #바로 else return 2 하면 단어 하나만 확인후 없으면 2 출력함