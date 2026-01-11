#문자열을 list 씌우면 전체 리스트 내 원소가 된다
#순환형에서는 len(a) 기준으로 나머지 처리 계산
def solution(A, B):
    if len(A) != len(B):
        return -1

    n = len(A)
    if n == 0:   # 혹시 빈 문자열 케이스가 있으면
        return 0

    double = A + A

    ans = None
    start = 0
    while True:
        i = double.find(B, start)
        if i == -1 or i >= n:     # 회전은 시작 위치가 0~n-1만 의미 있음
            break

        k = (n - i) % n           # i(왼쪽 이동) -> 오른쪽 이동 횟수
        ans = k if ans is None else min(ans, k)

        start = i + 1             # 다음 매치 위치 탐색

    return -1 if ans is None else ans
