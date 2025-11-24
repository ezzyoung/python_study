def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0 #하나라도 다르면 0
    return 1 #모두 같으면 1