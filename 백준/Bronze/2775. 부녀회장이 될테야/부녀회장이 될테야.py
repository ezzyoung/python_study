t = int(input())
for _ in range(t):
    floor = int(input()) #층
    door = int(input()) #호
    f0 = [x for x in range(1,door+1)] #0층에 사는 사람 수
    for k in range(floor): #층 수만큼 업데이트
        for i in range(1,door):
            f0[i]+=f0[i-1] #업데이트
    print(f0[-1])
            
        