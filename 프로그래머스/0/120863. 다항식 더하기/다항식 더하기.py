'''
+ 기준으로 나눠야 함
for t in terms:
    ...
else:
    ...
여기서 for else 의 경우 같은 선상에 쓰며, for 문 반복할대로 반복후 else 작동
'''
def solution(polynomial):
    terms = polynomial.split('+')  # + 기준으로 나눔 (공백 처리 필요)
    x_front = 0
    num = 0

    for t in terms:
        t = t.strip()  # 공백 제거 (핵심!)
        if 'x' in t:
            if t == 'x':
                x_front += 1
            else:
                x_front += int(t[:-1])  # '7x' -> 7
        else:
            num += int(t)

    parts = []
    if x_front:
        parts.append('x' if x_front == 1 else f'{x_front}x')
    if num:
        parts.append(str(num))

    return " + ".join(parts)
