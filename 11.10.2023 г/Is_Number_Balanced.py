def sum_of_digits(number):
    sum=0
    while number!=0:
        sum=sum+number%10
        number=number//10
    return sum    
def digitcounting(number):
    number1=number
    count=0
    while number1!=0:
        number1=number1//10
        count=count+1
    return count    
def is_balanced(number):
    digitscount=digitcounting(number)
    if digitscount==1:
        return 1
    if digitscount%2==0:
        digitscount1=digitscount/2
        half1=number//10**digitscount1
        half2=number%10**digitscount1
        sum1=sum_of_digits(half1)
        sum2=sum_of_digits(half2)
        if sum1==sum2:
            return 1
        else: 
            return 0
    if digitscount%2==1:
        digitscount1=digitscount//2
        half1=number//10**(digitscount1+1)
        half2=number%10**digitscount1
        sum1=sum_of_digits(half1)
        sum2=sum_of_digits(half2)
        if sum1==sum2:
            return 1
        else: 
            return 0   

if __name__=='__main__':
    number=int(input("enter value:"))
    ok=is_balanced(number)
    if ok==1:
        print("true")
    else:
        print("false")    
       