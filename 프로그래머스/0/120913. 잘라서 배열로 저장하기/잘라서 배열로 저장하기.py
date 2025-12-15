def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0,len(my_str),n)] #n길이만큼 띄어서 반환