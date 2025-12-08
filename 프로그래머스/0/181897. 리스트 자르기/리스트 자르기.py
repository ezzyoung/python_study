def solution(n, slicer, num_list):
    a,b,c = slicer
    if n ==1:
        return num_list[:b+1]
    elif n ==2:
        return num_list[a:]
    elif n==3:
        return num_list[a:b+1]
    elif n==4:
        return num_list[a:b+1:c] #인덱스 마지막 값은 포함 안되니까 특정 인덱스까지 가능하려면 이렇게 해야 함