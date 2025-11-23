#문제에서 묶는다고 해서 나도 묶을 필요는 없다는 점 인지
def solution(names):
    return [names[i] for i in range(0, len(names),5)] #리스트 형식, 전체 인덱스 중 5씩 건너뛰어 앞
    