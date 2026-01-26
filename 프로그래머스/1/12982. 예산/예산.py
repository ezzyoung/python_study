def solution(d, budget):
    d.sort() #작은값 -> 큰값
    cnt = 0
    
    for cost in d:
        if budget < cost:
            break
        budget -= cost #점진적으로 빼
        cnt += 1
    return cnt