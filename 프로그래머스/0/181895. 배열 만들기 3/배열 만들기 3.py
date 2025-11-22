def solution(arr, intervals):
    (a1,b1),(a2,b2) = intervals #특정 형식이 주어지면 나눠서 추출 가능
    front = arr[a1:b1+1]
    back = arr[a2:b2+1]
    return front + back