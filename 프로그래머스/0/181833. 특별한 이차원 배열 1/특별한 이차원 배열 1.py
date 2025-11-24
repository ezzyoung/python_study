def solution(n):
    answer = [[0]*n for _ in range(n)] #정사각행렬 지정
    for i in range(n):
        answer[i][i] = 1 #대입은 단순 등호
    return answer
        