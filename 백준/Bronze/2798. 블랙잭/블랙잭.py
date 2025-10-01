N, M = map(int,input().split())
numbers = list(map(int, input().split()))
result = 0
for i in range(N): #이게 가능한 이유는 i 가 N-1 까지 도는데 numbers 리스트의 인덱스로 들어간다고 생각하면 되기 때문
    for j in range(i+1,N):
        for h in range(j+1,N):
            if (numbers[i]+numbers[j]+numbers[h])>M:
                continue
            else:
                result = max(result,(numbers[i]+numbers[j]+numbers[h]))
print(result)