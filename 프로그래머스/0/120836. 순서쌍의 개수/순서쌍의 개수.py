def solution(n): #이런 거꾸로 곱셈 순서쌍은 순서쌍을 구하는게 문제가 아니라 약수가 몇개이지?
    sum = 0
    for i in range(1, n+1):
        if n%i == 0:
            sum+=1
    return sum
    