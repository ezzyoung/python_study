def solution(my_string, alp):
    if alp in my_string:
        my_string = my_string.replace(alp, alp.upper()) #바꿈
        return my_string
    else:
        return my_string