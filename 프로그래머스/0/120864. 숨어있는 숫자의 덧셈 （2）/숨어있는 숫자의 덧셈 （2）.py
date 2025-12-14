import re

def solution(my_string):
    numb = re.findall(r'\d+',my_string) #숫자 찾는 정규표현식
    return sum(map(int,numb))