def fibonacci_numbers(number):
    a=1
    b=1
    i=1
    while i<=number:
        print(a)
        c=b
        b=a+b
        a=c
        i=i+1


if __name__=='__main__':
    number=int(input("enter value:"))
    fibonacci=fibonacci_numbers(number)
    print(fibonacci)