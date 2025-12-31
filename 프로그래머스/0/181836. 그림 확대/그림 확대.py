def solution(picture, k):
    answer = []
    for row in picture:
        expand = ''.join(c*k for c in row) #각 n 배
        for _ in range(k):
            answer.append(expand) 
    
    return answer