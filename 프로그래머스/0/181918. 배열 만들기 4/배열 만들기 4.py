def solution(arr):
    stk = []
    i = 0
    while i < len(arr): #arr 의 길이와 비교해야 하는 부분
        if not stk:
            stk.append(arr[i])
            i+=1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i+=1
        else:
            stk.pop()
    return stk