N = int(input())
score = list(map(int,input().split()))
now_score=[]
answer = 0
for i in range(N):
    new = score[i] / max(score)*100 
    now_score.append(new)

answer = sum(now_score)
print(answer/N)

    