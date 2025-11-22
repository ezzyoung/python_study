def solution(todo_list, finished):#zip : 여러개 리스트를 인덱스 순서대로 묶어줌
    return [todo for todo, done in zip(todo_list,finished)if not done] #if not done 이 true 반대
        