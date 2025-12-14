from collections import Counter
def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    difference = participant_count - completion_count
    
    # 리스트 형태의 키들을 문자열로 결합하여 반환
    return ", ".join(difference.keys())


            

        