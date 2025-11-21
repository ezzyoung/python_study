def solution(arr):#[ <값> for 변수 in 리스트 ], [ <조건이면 값1 else 값2> for 변수 in 리스트 ]
    return [i//2 if (i>=50 and i%2 ==0)
           else i*2 if (i<50 and i%2 ==1)
           else i for i in arr]
