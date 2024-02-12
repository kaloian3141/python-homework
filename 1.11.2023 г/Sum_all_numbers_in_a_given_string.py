def sum_of_numbers(st):
    sum = 0  
    current_number = ""  
    digits = "0123456789"  
    i = 0
    while i < len(st):
        char = st[i]
        if char in digits:   
            current_number += char
        else:
            if current_number:
               sum += int(current_number)
            current_number = ""
        i += 1    
    if current_number:
        sum += int(current_number)
    
    return sum

if __name__=='__main__':    
    st = "21g3g3"
    sum=sum_of_numbers(st)
    print(sum)