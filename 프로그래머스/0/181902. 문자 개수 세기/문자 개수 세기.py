def solution(my_string):
    numbers = [0]*52
    for ch in my_string:
        if 'A'<=ch<='Z':
            numbers[ord(ch)-ord('A')] += 1
        else:
            numbers[26+ord(ch)-ord('a')] += 1
    return numbers
            