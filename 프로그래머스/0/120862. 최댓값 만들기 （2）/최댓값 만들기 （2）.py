'''
음수 두개 곱 vs 양수 두개 가장 큰거 곱을 결국 비교해서 가장 큰 수를 반환한다.
'''
def solution(numbers):
    numbers.sort() #오름차순
    sol1 = numbers[-1]*numbers[-2]
    sol2 = numbers[0]*numbers[1]
    return max(sol1, sol2)