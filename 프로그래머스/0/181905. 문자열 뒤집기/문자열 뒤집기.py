def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:] #문자열은 더할 수 있다,
#인덱스는 끝부분은 -1까지, 시작은 시작부터