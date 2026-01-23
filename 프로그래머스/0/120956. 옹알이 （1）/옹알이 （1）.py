def solution(babbling):
    result = 0
    pos = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        prev = ''#이전에 받을 단어 빈 문자열에 두기
        ok = True
        
        while b:
            matched = False #초기화로 발음 가능 없다고 하기
            for p in pos:
                if b.startswith(p) and p != prev:
                    b = b[len(p):] #앞부분 잘라내기
                    prev = p
                    matched = True
                    break #계속 돌아
            if not matched:
                ok = False
                break
                    
        if ok:
            result+=1
            
    return result
            
                