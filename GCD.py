#a program that finds the GCD of the two  numbers 

def gcd(m, n):
    while n!=0:
        m,n = n,m % n
        return m
    m=int(input("Enter the first number:"))
    n=int(input("Enter the second number:"))

    print(f"The greatesncommon divisor of {m} and {n} is {gcd(m,n)}.")

    