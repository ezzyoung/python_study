def solution(arr):
    if 2 not in arr:
        return [-1] #먼저 설정 : 2 없으면 아래 반환 안되니까
    start = arr.index(2)
    end = len(arr)-1-arr[::-1].index(2) #뒤집었을 때 2 나오는 인덱스 찾아라

    return arr[start:end+1] #마지막은 포함 안함