#정수를 이진 문자열로 바꿀 수 있는 내장함수가 있음 bin()
def solution(bin1, bin2):
    return bin(int(bin1,2) + int(bin2, 2))[2:] #ob 없애기
    