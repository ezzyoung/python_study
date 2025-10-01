n = input()
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    for i in range(2,num+1): #num 을 num 아래 모든 숫자들로 나눠봐
        if num%i == 0:     
            if i == num: #그 중 i 와 num 같을때
                count+=1
            break
print(count)