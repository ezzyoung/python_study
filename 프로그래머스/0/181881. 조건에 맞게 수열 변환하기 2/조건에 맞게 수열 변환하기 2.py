def solution(arr):
    x = 0
    while True:
        arr2 = []
        for i in arr:
            if i >= 50 and i%2==0:
                arr2.append(i//2)
            elif i<=50 and i%2==1:
                arr2.append(i*2+1)
            else:
                arr2.append(i)
                
        if arr == arr2:
            return x
        arr = arr2 #갱신시킴
        x+=1
        
        
            
    