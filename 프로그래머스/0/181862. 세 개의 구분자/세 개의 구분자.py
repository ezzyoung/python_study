def solution(myStr):
    for ch in ["a","b","c"]:
        myStr = myStr.replace(ch," ") #변수 저장
    result = myStr.split() #빈칸으로 나누기
    
    return result if result else ["EMPTY"]
        