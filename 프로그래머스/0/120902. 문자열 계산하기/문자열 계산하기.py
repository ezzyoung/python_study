def solution(my_string):
    m = my_string.split(' ')
    result = int(m[0])
    for i in range(1,len(m),2):
        if m[i] == '+':
            result+=int(m[i+1])
        else:
            result-=int(m[i+1])
    return result
    