def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = sum(months[:(a-1)]) + b
    return days[(total_days+5-1)%7]