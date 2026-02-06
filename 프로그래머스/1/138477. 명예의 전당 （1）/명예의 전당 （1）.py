import heapq

def solution(k, score):
    hall=[] #명예의 전당
    answer =[] #최종 반환할것
    for s in score:
        heapq.heappush(hall,s) #heapq - 항상 작은값(큰값) 바로 빼낼수 있는 자료구조
    
        if len(hall)>k:
            heapq.heappop(hall) #하나씩 뽑아냄
    
        answer.append(hall[0]) #작은거 누적
    return answer