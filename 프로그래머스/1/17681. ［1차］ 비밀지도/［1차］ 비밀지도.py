def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        combined = a|b #하나라도 벽이면 벽
        
        row = format(combined, f'0{n}b') #크기가 n 인 지도이니 자리수 맞춰 2진법
        row = row.replace('1','#').replace('0',' ')
        
        answer.append(row)
        
    return answer