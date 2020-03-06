def fib(n):
    # Write Fibonacci Series upto order n
    a,b=0,1
    while a<n:
        print a,
        a,b=b,a+b

n=input("Order of Fibonacci Series: ")
fib(n)
