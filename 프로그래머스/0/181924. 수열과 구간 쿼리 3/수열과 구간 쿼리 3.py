def solution(arr, queries):#queries 처럼 패턴이 있는 경우 그냥 i,j 로도 가능
    for i,j in queries:
        arr[i],arr[j]=arr[j],arr[i]
    return arr