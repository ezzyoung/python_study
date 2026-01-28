'''
Combination 쓸 수 있다면 쓰기 + 삼중문이 일반적
필터링 할때는 굳이 else 넣을 필요 없음
직관적 풀이는 3중문
'''
from itertools import combinations
def solution(number):
    return sum(1 for a,b,c in combinations(number,3) if a+b+c == 0)