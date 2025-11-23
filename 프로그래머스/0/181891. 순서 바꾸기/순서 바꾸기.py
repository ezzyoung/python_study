def solution(num_list, n):#복잡하게 생각하지 말고 slicing 후 붙여
    return num_list[n:] + num_list[:n] #슬라이싱 할때 앞에 있으면 해당 인덱스 포함, 뒤에 있으면 해당 인덱스 미포함