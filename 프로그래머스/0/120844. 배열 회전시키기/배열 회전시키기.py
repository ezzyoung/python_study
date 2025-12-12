'''
리스트 문제 → 슬라이싱 먼저 떠올리기
인덱스 리스트를 따로 만들면 대부분 과설계
'''
def solution(numbers, direction):
    if direction == 'right':
        return [numbers[-1]] + numbers[:-1] #마지막 인덱스는 포함 X, 리스트끼리 더할 수 있다
    elif direction == 'left':
        return numbers[1:] + [numbers[0]]