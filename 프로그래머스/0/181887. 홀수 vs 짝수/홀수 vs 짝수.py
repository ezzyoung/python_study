def solution(num_list):
    odd_sum = 0   # 홀수 번째 원소 합
    even_sum = 0  # 짝수 번째 원소 합

    for i in range(len(num_list)):
        if (i + 1) % 2 == 1:      # 홀수번째 인덱스
            odd_sum += num_list[i]
        else:                    # 짝수 번째
            even_sum += num_list[i]
    return max(odd_sum, even_sum)
