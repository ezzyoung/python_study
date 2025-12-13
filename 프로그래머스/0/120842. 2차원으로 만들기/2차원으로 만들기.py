def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)] #n씩 끊어서 넣고 그걸 전부 리스트로 감싼것
        