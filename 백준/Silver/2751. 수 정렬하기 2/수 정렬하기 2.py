import sys
n = int(input()) #숫자 입력
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()
for i in num:
    print(i)