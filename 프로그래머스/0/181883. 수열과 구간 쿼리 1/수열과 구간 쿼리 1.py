def solution(arr, queries):#리스트가 특정 형식을 따르면 변수1, 변수2 꼴로 나타내기 가능
    for s,e in queries:
        for i in range(s,e+1):
            arr[i]+=1 #arr 의 특정 인덱스 값에 1 더함
    return arr