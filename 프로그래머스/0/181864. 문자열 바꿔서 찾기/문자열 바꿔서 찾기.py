def solution(myString, pat):
    swapped = ''.join('B'if ch == 'A'else'A'for ch in myString) #join 으로 빈 문자열에 연결
    return 1 if pat in swapped else 0 #한줄