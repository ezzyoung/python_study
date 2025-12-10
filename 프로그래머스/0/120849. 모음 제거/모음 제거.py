def solution(my_string):
    moem = ['a','e','i','o','u']
    return ''.join(i for i in my_string if i not in moem) #리스트컴프리헨션 활용