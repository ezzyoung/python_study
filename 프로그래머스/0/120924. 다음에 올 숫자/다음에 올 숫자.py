def solution(common):
    if common[1]-common[0] == common[2]-common[1]:
        ap = common[1]-common[0]
        return common[-1]+ap
    else:
        rep = common[1]//common[0]
        return common[-1]*rep