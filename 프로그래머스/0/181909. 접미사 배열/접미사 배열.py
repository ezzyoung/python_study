def solution(my_string):
    suffixes = [my_string[i:]for i in range(len(my_string))]
    return sorted(suffixes) #suffix 알파벳 순으로 배열
    