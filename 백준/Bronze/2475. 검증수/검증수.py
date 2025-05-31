#여러가지 수 입력받으면 무조건 리스트 사용
k = list(map(int,input().split()))
b = 0
for i in range(5): #0-4
    b += k[i]**2
print(b%10) #b 10으로 나눈 나머지