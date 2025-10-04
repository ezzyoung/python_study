n = int(input())
nums_pileup = 1 #벌집 개수
cnt = 1
while n > nums_pileup:
    nums_pileup+=6*cnt #6씩 늘려 인풋과 비교해야 하니까
    cnt += 1 #벌집 수는 하나씩 늘려
print(cnt)