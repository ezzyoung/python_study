def solution(arr, queries):
    result = []
    for s,e,k in queries:
        cand = [arr[i] for i in range(s,e+1) if arr[i]>k] #후보들
        result.append(min(cand) if cand else -1) #결과 있으면 추가 아니면 -1
    return result
        
        