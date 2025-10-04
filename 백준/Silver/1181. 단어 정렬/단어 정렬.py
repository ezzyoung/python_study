import sys
n = int(sys.stdin.readline()) #입력
lst = []
for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst) #중복 단어 제거
lst = list(set_lst) #중복 제거 후 다시 리스트화
lst.sort()
lst.sort(key=len) #두단계로 나눠
for i in lst:
    print(i)