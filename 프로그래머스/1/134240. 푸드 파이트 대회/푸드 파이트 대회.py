def solution(food):
    ans = [] #빈 리스트 준비
    for i in range(len(food)):
        ans.append(str(i)*(food[i]//2))
    leftstr = ''.join(ans)
    return leftstr + '0' + leftstr[::-1]