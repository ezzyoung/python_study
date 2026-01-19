def solution(board):
    n = len(board)
    danger = [[False]*n for _ in range(n)] #안전으로 초기화
    directions = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
    
    for i in range(n):
        for j in range(n):
            
            if board[i][j] == 1:
                danger[i][j] = True 
                
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    
                    if 0<= ni <n and 0 <=nj <n:
                        danger[ni][nj] = True
                        
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if not danger[i][j]:
                safe_count += 1
                
    return safe_count