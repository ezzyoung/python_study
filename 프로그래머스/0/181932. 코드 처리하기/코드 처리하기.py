def solution(code):
    ret = []
    mode = 0
    
    for i, ch in enumerate(code):
        if ch == "1":
            mode = 1-mode #0,1변환
        else:
            if mode ==0 and i%2==0:
                ret.append(ch)
            elif mode ==1 and i%2==1:
                ret.append(ch)
    answer = ''.join(ret)
    return answer if answer else "EMPTY"