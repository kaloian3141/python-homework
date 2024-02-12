def sum_of_digits(number):
    sum = 0
    while number!=0:
        digit=number % 10
        sum=sum+digit
        number=number//10
    return sum

if __name__=='__main__':
    number = int(input('enter value:'))
    result=sum_of_digits(number)
    print(result)