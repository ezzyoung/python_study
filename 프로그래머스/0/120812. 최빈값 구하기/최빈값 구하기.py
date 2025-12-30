def solution(array):
    real = list(set(array)) 
    k = []
    for i in real:
        k.append(array.count(i))
    if k.count(max(k)) >1:
        return -1
    return real[k.index(max(k))]