def solution(arr, flag):
    x=[]
    for i, j in zip(arr,flag):
        if j:
            x.extend([i]*(i*2)) #[i]배열을 i*2
        else:
            x = x[:-i] #x 라는 리스트에서 i 개 제외 가져와라
    return x