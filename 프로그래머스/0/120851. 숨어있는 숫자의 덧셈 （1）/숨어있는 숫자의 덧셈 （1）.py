def solution(my_string):
    return sum(int(ch) for ch in my_string if ch.isdigit())

#i.isdigit() 은 true false 로 반환하니 if ch.isdigit() 으로도 자동으로 TRUE 일때반 반환한다 정보