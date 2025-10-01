while True:
    n = input()
    if n == '0':
        break
    else:
        if n == n[::-1]:#선순과 거꾸로 동일
            print("yes")
        else:
            print("no")