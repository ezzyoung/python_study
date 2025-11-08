def solution(arr, n):
    if len(arr)%2 == 0:
        for i in range(1,len(arr),2):
            arr[i]+=n #홀수 인덱스에만 n 더해
    else:
        for i in range(0, len(arr), 2):
            arr[i]+=n
    return arr