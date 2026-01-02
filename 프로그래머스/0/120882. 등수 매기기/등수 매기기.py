def solution(score):
    sums = [s[0] + s[1] for s in score]
    sums_real = sorted(sums, reverse=True) #큰 수부터
    
    rank = []
    for s in sums:
        rank.append(sums_real.index(s) +1) #인덱스 추출 및 더하기 1
    
    return rank