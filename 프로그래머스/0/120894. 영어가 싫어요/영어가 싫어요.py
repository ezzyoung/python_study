'''
딕셔너리화 해서 key value 쓸때는 key, values() 말고 for 문 돌려 replace
items() 하면 튜플 형태로 key, value 나옴
replace 는 문자열만 바꿀 수 있음
'''
def solution(numbers):
    answer = {"zero":"0", 
              "one":"1",
              "two":"2",
              "three":"3",
              "four":"4",
              "five":"5",
              "six":"6",
              "seven":"7",
              "eight":"8",
              "nine":"9" }
    for key in answer:
        numbers = numbers.replace(key, answer[key]) #replace 는 원본을 바꾸지 않음 변수에 다시 저장해야함
    return int(numbers)
    
            