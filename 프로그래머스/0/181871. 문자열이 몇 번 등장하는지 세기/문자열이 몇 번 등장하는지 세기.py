def solution(myString, pat):
    count = 0
    for i in range(len(myString)-len(pat)+1): #range 는 뒷부분은 마지막 포함 안함
        if myString[i:i+len(pat)] == pat:
            count+=1
    return count