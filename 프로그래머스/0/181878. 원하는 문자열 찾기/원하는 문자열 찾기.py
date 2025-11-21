def solution(myString, pat):
    mystring = myString.lower()
    pati = pat.lower()
    if pati in mystring:
        return 1
    else:
        return 0