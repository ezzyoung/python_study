def solution(my_string, queries):
    for s, q in queries:
        my_string = (
        my_string[:s]+
        my_string[s:q+1][::-1]+ #거꾸로
        my_string[q+1:]
        )
    return my_string