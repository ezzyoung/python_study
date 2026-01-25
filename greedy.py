'''
그리디 알고리즘 : 매 단계마다 전체 최적해 고려하지 않고 현재 상황에서 가장 좋아보이는 선택부터 하는 알고리즘
이걸 반복 -> 최종 해답 도출

아이디어 : 
나누는 작업을 많이 하면 정답에 가까워진다
'''
n, k = map(int, input().split())
result = 0

#while True 쓰는 이유 : 무조건 반복하고, 멈출때 내가 멈춘다
while True:
    #N 이 K 로 나눠떨어지는 수가 될때까지 빼고, 가장 근접하는 k 배수 찾기
    target = (n // k) * k
    result += (n - target)
    n = target #하나씩 뺄만한거 더해
    if n<k:
        break #n 을 더 이상 k 로 나눌 수 없을때 반복문 탈출
    result +=1 #result 누적
    n//=k #K로 나누기

result += (n-1) # 마지막으로 남은 수에 대하여 1씩 빼기
print(result)
