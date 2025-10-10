n = int(input()) #몇명 입력할건지 설정
member_list =[]
for i in range(n):
    age, name = map(str, input().split()) #나이, 이름 입력받기, 공백 제거
    age = int(age)
    member_list.append((age,name))
member_list.sort(key = lambda x:x[0]) #정렬 기준 정할때 key
for i in member_list:
    print(i[0], i[1])