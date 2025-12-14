def solution(i, j, k):
    ans =0
    for l in range(i,j+1):
        for m in str(l):
            if m==str(k):
                ans+=1
    return ans