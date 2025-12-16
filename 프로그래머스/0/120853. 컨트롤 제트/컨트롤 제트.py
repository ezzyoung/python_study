'''
stack problem : last in first out
'''
def solution(s):
    s = s.split(' ')
    a = []
    for i in s:
        if i == 'Z':
            a.pop()
        else:
            a.append(int(i))
    return sum(a)