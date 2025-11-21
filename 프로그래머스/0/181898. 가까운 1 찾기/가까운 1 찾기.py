def solution(arr, idx):#순차적으로 찾을 때는 range 쓴다고 생각하자
    for i in range(idx, len(arr)): #idx 보다 크고 len(arr)인 마지막 길이보다 작아야 함
        if arr[i] == 1:
            return i 
    return -1 #탐색 전체 다 하고 보게 하려면 이렇게 해야 한다