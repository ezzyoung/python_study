def solution(wallet, bill):
    num = 0 
    while max(wallet)<max(bill) or min(wallet)<min(bill):
        if bill[0]>=bill[1]:
            bill[0] = bill[0]//2
            num+=1
        else:
            bill[1] = bill[1]//2
            num+=1
    return num
        
    