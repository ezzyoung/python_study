def solution(arr):
    i = 0
    stk =[]
    
    while i<len(arr):
        if not stk: #배열에 아무것도 없으면
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop() #마지막 원소 제거는 pop
            else:
                stk.append(arr[i])
                
        i+=1

    return stk if stk else [-1] #조건부 있는 리턴은 이렇게 한줄로 쓸수 있음