def solution(rsp):
    gbb = {'2':'0', '0':'5', '5':'2'} #바로 문자열
    return ''.join(gbb[i] for i in rsp)