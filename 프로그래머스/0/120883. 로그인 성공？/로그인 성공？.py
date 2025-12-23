'''
이차원 배열은 a, b 로 우선 나누고 시작하자
'''
def solution(id_pw, db):
    userid, userpw = id_pw
    
    for db_id, db_pw in db:
        if userid == db_id:
            if userpw == db_pw:
                return "login"
            else:
                return "wrong pw"
            
    return "fail"
        