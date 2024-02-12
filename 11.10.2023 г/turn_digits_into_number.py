def turn_digits_into_number(digits):
    number=0
    j=0
    i=6
    while i>=0:
        number=number+digits[i]*(10**j)
        j=j+1
        i=i-1
    return number
    
if __name__=='__main__':
    digits=[1,3,4,1,3,5,3]
    number=turn_digits_into_number(digits)  
    print(number)  
   

