def solution(n):
    num=[]
    while n>0:
        if n%2!=0:
            num.append(n)
            n=n-2
        else:
            num.append(n-1)
            n=n-3
    num.sort()
    return num