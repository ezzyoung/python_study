#순서 보존에 집중
def solution(my_string):
    result = ''
    for ch in my_string:
        if ch not in result:
            result +=ch #문자열에 문자 더할 수 있음
    return result