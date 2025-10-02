n = int(input())
result = 0
for i in range(2,n+1):
    nums = list(map(int, str(i))) #각 숫자별 합
    result = i + sum(nums) #생성자 + 숫자별 합
    if result == n:
        print(i)
        break
else:
    print(0)