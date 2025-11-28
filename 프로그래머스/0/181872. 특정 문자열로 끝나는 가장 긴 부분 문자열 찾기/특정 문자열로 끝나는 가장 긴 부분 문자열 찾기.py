def solution(myString, pat):
    #rfind() - 가장 마지막에 특정 문자열이 나오는 인덱스 반환 + 길이 더해
    return myString[:myString.rfind(pat)+len(pat)] 