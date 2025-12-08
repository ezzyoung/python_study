def solution(arr, queries):
    for s,e,k in queries:
        for i in range(s,e+1):
            if i%k == 0:
                arr[i]+=1 #하나씩 더해가는 상황
    return arr #완전 바깥으로 빼야지 전체를 돈다