'''
sorted - 작은게 먼저 앞
(abs, n)
정렬을 key 기준에 맞춰 정렬. 리스트도 key 기준 있을 수 있음
'''
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), -x))

    
        