def solution(numbers):
    sum1 = []
    for i in range(10):
        if i not in numbers:
            sum1.append(i)
    return sum(sum1)
            