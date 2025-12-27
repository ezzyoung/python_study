def solution(dots):
    a = [dot[0] for dot in dots]
    b = [dot[1] for dot in dots]
    result = (max(a) - min(a))*(max(b) - min(b))
    return result