'''
for i, x in enumerate(arr):
    print(i, x)
즉 enumerate 는 인덱스와 값 둘 다 빼주는 함수
인덱스의 홀짝을 나누려면 인덱스와 값 둘다 빼야 하므로 사용
'''
def solution(arr, query):
    for i,x in enumerate(query):
        if i%2 == 0:
            arr = arr[:x+1]
        else:
            arr = arr[x:]
    return arr
    