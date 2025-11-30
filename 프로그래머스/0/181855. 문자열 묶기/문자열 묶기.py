'''
길이별로 그룹별로 묶어야 하니 딕셔너리
딕셔너리에 값이 있나 if l in dic 가면, 키를 검색한다
dic[i] = value
'''
def solution(strArr):
    dic = {} #딕셔너리
    for i in strArr:
        l = len(i)
        if l in dic:
            dic[l]+=1
        else:
            dic[l]=1
    
    return max(dic.values())