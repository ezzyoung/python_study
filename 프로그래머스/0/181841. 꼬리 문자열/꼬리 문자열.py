def solution(str_list, ex): #문자열로 반환하니 join
    return ''.join(s for s in str_list if ex not in s) #문자열은 포함 미포함 바로 in i 이런거 안써도 가능
    