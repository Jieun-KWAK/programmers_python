def solution(n):
    num=[]
    if n%2==0:
        for i in range(2, n+1 ,2):
            num.append(i)
    else :
        for i in range(2, n+1 ,2):
            num.append(i)
    return sum(num)