def solution(s):
    answer=[]
    for k in s:
        if s.count(k) == 1:
            answer.append(k)
    return ''.join(sorted(answer))