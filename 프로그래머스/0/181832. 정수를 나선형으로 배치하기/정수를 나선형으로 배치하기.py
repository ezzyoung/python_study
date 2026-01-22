def solution(n):
    result = [[0]*n for _ in range(n)]
    x, y =0,0
    num =1
    directions = [(0,1), (1,0), (0,-1),(-1,0)]
    dir_idx = 0
    
    #일단 num 은 n*n 범위 내에서 돌아가야 함
    
    while num <= n*n:
        result[x][y] = num
        num+=1
        
        #다음 위치 계산
        nx = x + directions[dir_idx][0]
        ny = y + directions[dir_idx][1]
        
        if nx<0 or ny<0 or nx>=n or ny>=n or result[nx][ny]!=0:
            dir_idx = (dir_idx+1)%4
            nx = x+directions[dir_idx][0]
            ny = y+directions[dir_idx][1]
            
        x, y = nx, ny
    
    return result