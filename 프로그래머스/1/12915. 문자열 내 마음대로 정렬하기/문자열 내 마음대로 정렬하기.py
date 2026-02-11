#sorted 에 key 튜플로 넣으면 특정 기준을 정할 수 있음
def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n],x))