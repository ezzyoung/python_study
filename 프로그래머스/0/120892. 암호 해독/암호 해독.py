def solution(cipher, code):
    return ''.join(cipher[i] for i in range(code-1, len(cipher),code)) #code-1 이 실제 n 번째 단어