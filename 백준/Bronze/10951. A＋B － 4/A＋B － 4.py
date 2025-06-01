#try, except 구문 사용 -- 기본적으로 try 사용, 오류 생기면 except 로 나가는 형식

while True:
    try :
        a, b = map(int,input().split())
        print(a+b)
    except:
        break