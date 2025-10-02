#생각 흐름 : factorial 함수를 만들자
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans*=i
    return ans

#콤비네이션 정의
answer = factorial(N)//(factorial(K)*factorial(N-K))
print(answer)