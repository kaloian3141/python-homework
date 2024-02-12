def turn_into_digits(number):
    digits_arr=[]
    secondnumber=0
    while number!=0:
        digit = number%10
        secondnumber=secondnumber*10+digit
        number=number//10
    while secondnumber!=0:
        secondnumber_digit =secondnumber%10
        digits_arr.append(secondnumber_digit)
        secondnumber=secondnumber//10
    print(digits_arr)    
    


if __name__=='__main__':
    number = int(input('enter value:'))
    turn_into_digits(number)