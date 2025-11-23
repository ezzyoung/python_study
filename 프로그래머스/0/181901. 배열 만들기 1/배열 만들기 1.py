def solution(n, k):
    return [j for j in range(k,n+1,k)] #리스트컴프리헨션 무조건 변수부터, range 는 앞은 포함, 뒤는 +1 해줘야 해당수 포함