def solution(number, limit, power):
    total = 0 #구해야 할 값 초기화
    for i in range(1, number+1):
        count = sum(1 for j in range(1,int(i**0.5)+1) if i%j ==0) #약수를 구할때는 해당 수의 루트 씌운 수까지 탐색하면 된다. 여기서는 잘반만 본 상태
        count = count*2 - (1 if int(i**0.5)**2 == i else 0) #제곱근인거는 1 빼
        total += power if count > limit else count #제한에 맞춰서 더해
        
    return total
        
        