N = int(input()) #사람수
size = list(map(int, input().split()))#사이즈 순대로 리스트에 넣기
T,P = map(int, input().split()) #티셔츠, 펜 한 묶음 수
t_bundle = 0 #티셔츠 묶음수
for sz in size:
    if sz == 0:
        continue
    elif sz <= T:
        t_bundle += 1
    elif sz % T == 0:
        t_bundle += sz//T
    else:
        t_bundle += (sz//T) +1
        
print(t_bundle)
print(N//P, N%P)