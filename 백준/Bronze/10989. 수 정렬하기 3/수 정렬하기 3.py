import sys
input = sys.stdin.readline

#N 입력
N = int(input())
#10001 칸을 가진 리스트 정의
count = [0]*10001
#N 개의 수를 뽑아온다
for _ in range(N):
    num = int(input())
    count[num]+=1
for i in range(10001):
    if count[i]!=0:
        for j in range(count[i]):
            print(i)