#이 문제랑은 상관없으나 숫자 -> 문자로 바꾼 후에는 for i in str 가능 ->  굳이 리스트로 이중변환 필요 X
def solution(num_list):
    sum1 = 0
    sum2 = 0
    for i in num_list:
        if i%2 == 0:
            sum1+=1
        elif i%2 ==1:
            sum2+=1 
    return [sum1, sum2]