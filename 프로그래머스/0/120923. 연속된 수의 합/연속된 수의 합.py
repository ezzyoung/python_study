def solution(num, total):
    a = (total - num*(num-1)//2) // num
    return [i for i in range(a, a+num)]
