def solution(arr1, arr2):
    return[
        [a+b for a, b in zip(r1, r2)]
        for r1, r2 in zip(arr1, arr2)
    ] #arr1, arr2 에서 원소 뽑아내고 그 원소의 원소를 더해서 배열로 만들어 반환