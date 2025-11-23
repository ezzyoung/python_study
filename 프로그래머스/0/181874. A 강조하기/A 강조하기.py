def solution(myString):
    real = myString.lower()
    if 'a' in real:
        return real.replace('a','A')
    else:
        return real