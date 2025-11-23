def solution(numLog):
    result ='' #result 를 구해야 하는 상황
    for i in range(1,len(numLog)):#인덱스 값조정
        gapx = numLog[i]-numLog[i-1]
        if gapx ==1:
            result+='w'
        elif gapx == -1:
            result+='s'
        elif gapx==10:
            result+='d'#문자열은 더하기
        elif gapx == -10:
            result+='a'
    return result #다 돌고 반환