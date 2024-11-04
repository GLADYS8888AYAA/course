#A program that computes and outputs the nth fabionacci number.

def fibonacci(n):
    if n <=0:
        return "Please enter a positive integer."
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        a,b=1,1
        for _ in range(3,n+1):
            a,b=b, a+b
            return b 