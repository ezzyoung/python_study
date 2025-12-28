def solution(arr, k):
    result = []
    seting = set() #만약 리스트 내에 set 가 있으면 set이 한뭉치로 들어가서 안됨
    
    for x in arr:
        if x not in seting:
            result.append(x)
            seting.add(x) #set 은 한번에 모든걸 같이 봄 hash table 로 생각함 즉 그 원소만 딱 확인
        if len(result) == k:
            break #k 같으면 끝
    
    return result+[-1]*(k-len(result))
        