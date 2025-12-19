def solution(arr):
    if len(arr) <= 1:
        return [-1]
    
    arr.remove(min(arr))   # 최솟값 1개만 제거
    return arr

        