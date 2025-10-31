def solution(myString):
    answer = ''
    for ch in myString:
        if ch<'l': #알파벳에서는 순서 지정으로 이보다 앞선 숫자 지정 가능
            answer += 'l'
        else:
            answer += ch #l 보다 아래 아닌애들은 그대로
    return answer