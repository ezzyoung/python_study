def solution(numbers):
    #pop 은 인덱스를 빼는거지 값을 빼는게 아님
    #sort - 다른 변수에 넣으면 none 됨 -> 원본을 수정하는 것
    #sorted - 원본은 바뀌지 않고 다른 변수에 할당됨 (변수 지정 가능), 오름차순
    numbers.sort()
    return numbers[-1]*numbers[-2]