'''
enumerate -> 인덱스, 문자열 함께 반환
'''
def solution(s):
    last = {} #마지막으로 등장하는 인덱스 및 문자
    answer =[] #정답용 리스트
    for idx, i in enumerate(s):
        if i in last:
            answer.append(idx-last[i])
        else:
            answer.append(-1)
        last[i] = idx #인덱스 갱신
    return answer
        