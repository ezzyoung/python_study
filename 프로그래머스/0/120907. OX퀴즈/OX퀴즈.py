'''
리스트 언패킹 - 리스트 요소 중 안쓰는걸 _ 빈칸화 해서 버리는용
'''
def solution(quiz):
    result = []
    
    for q in quiz:
        x, y, z, _, r = q.split()
        
        x= int(x)
        z= int(z)
        r= int(r)
    
        calc = x+z if y=="+" else x-z
        result.append("O" if calc==r else "X") 
        
    return result

            