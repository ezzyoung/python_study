def solution(q, r, code):
    return ''.join(code[i] for i in range(len(code)) if i%q ==r) #한줄로 하면 인덱스부터.
#문자열도 똑같이 인덱스화 가능, for i in range(a) 는 ai 미포함 0-a-1 까지
#나머지가 r 일때 i 구하려면 저렇게
    