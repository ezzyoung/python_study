def solution(numbers, k):
    n = len(numbers) #전체 길이 - 나눠줘야 하니까
    idx = (2*(k-1))%n #순환 고려해서 나눔 나머지
    return numbers[idx]