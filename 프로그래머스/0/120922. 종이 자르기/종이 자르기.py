def solution(M, N):
    srz = 0
    M, N = max(M,N), min(M,N)
    srz+=((N-1) + (M-1)*N)
    return srz