def solution(intStrs, k, s, l):
    answer=[]
    for i in intStrs:
        num = int(i[s:s+l])
        if num>int(k):
            answer.append(num) 
    return answer #다 돌고 append 해야 하니까