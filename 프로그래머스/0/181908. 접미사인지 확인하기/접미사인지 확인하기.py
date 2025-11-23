#endswith 라는걸 쓰면 뒤에서부터 보게 된다
def solution(my_string, is_suffix):
    return 1 if my_string.endswith(is_suffix) else 0 #뒤에서부터 보게 된 구조