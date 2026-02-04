def solution(numbers):
    s = set() #겹치면 안됨
    n = len(numbers) #몇개인가
    for i in range(n):
        for j in range(i+1, n):
            s.add(numbers[i] + numbers[j])
    return sorted(s) #오름차순