def solution(arr):
    cnt=1
    n=len(arr)
    while cnt<n: #while 문 이용
        cnt*=2 #거듭제곱
    return arr + [0]*(cnt-n)
        