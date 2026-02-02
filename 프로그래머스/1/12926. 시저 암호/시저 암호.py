def solution(s, n):
    result = []
    n %= 26  # 알파벳 개수로 나눈 나머지
    
    for ch in s:
        if 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + n) % 26 + ord('A'))) #순환
        elif 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + n) % 26 + ord('a'))) #순환
        else:
            result.append(ch)  # 공백 유지
    
    return ''.join(result)
