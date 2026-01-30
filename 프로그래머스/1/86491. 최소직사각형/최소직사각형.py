'''
결국 긴 변 중 최대와 짧은 변 중 최대를 구해야 함
'''
def solution(sizes):
    max_w = 0 # 긴변 중 최대
    max_h = 0 # 짧은변 중 최대
    for w, h in sizes:
        big = max(w,h)
        small = min(w,h)
        max_w = max(big, max_w)
        max_h = max(small, max_h)
    return max_w*max_h