'''
파이썬에서 반복 횟수만 필요하고 변수는 필요 없다면 for _ in range (빈칸)
'''
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*'*a)
