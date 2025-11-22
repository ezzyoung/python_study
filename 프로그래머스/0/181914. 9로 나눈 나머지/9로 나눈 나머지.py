def solution(number):
    nums = number.split() #split 쓰면 문자열 -> 리스트
    return sum(int(i) for i in nums)%9