def solution(n):
    answer=0
    for num in range(1, n+1):
        if n%num==0:
            answer=answer+1
    return answer