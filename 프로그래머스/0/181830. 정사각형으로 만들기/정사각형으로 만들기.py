'''
정사각행렬 -> 부족하면 채워넣는다
row, col, size 비교 생각
'''
def solution(arr):
    row = len(arr)
    col = len(arr[0]) #굳이 i, j 거릴 이유 없음
    size = max(row, col)
    for i in range(row):
        arr[i] += [0]*(size-col)
        
    for _ in range(size - row):
        arr.append([0] * size)

    return arr