def solution(str1, str2): #길이가 같고 번갈아 보여야 한다 -- zip (짝지어줌)
    result = ''
    for a, b in zip(str1, str2):
        result += a+b
    return result #전체 다 돌아야 하는 경우 return 어디다 둘지 잘 생각해야 함