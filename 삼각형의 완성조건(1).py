def solution(sides):
    line = max(sides)
    k = sum(sides)-line
    if k>line:
        return 1
    else : 
        return 2