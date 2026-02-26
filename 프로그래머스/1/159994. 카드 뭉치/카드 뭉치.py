#그리디 알고리즘으로 순차
def solution(cards1, cards2, goal):
    i = 0
    j = 0
    
    for words in goal: #goal 내 단어들 순회, 탐색 순서 정해주기
        if i < len(cards1) and cards1[i] == words:
            i+=1
        elif j < len(cards2) and cards2[j] == words:
            j+=1
        else:
            return "No"
        
    return "Yes" #for 문과 같은 선에 두면 다 돌고 완료후 -> Yes 출력 
        
        
        