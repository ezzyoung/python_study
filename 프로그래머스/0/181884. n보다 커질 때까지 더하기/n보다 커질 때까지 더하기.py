def solution(numbers, n):
    s = 0 #합 
    for i in numbers:
        s+=i #numbers 내에 있는 i
        if s>n:
            return s