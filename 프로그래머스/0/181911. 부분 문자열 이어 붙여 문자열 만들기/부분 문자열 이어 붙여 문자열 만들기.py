def solution(my_strings, parts):
    result = '' #최종반환용 초기화
    for s, (start, end) in zip(my_strings, parts):
        result +=s[start:end+1] #계속 반복문 돌게 해야 함
    return result