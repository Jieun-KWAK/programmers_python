def solution(slice, n):
    answer=0
    while answer>-1:
        answer+=1
        if slice*answer>=n:
            return answer