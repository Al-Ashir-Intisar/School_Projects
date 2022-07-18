def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        frst_term=0
        scnd_term=1
        temp1=0
        temp2=0
        while n>=2:
            temp2=scnd_term
            temp1=frst_term
            frst_term=temp2
            scnd_term=temp1+temp2
            n=n-1
        return frst_term




print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(7))
print(fibonacci(10))
print(fibonacci(25))
print(fibonacci(50))