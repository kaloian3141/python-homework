def are_pair(input_arr,sum):
    i=0
    while i<len(input_arr):
        j=i+1
        while j<len(input_arr):
            if input_arr[i]+input_arr[j]==10:
                print(i,j)
            j+=1    
        i+=1       

        

if __name__ == '__main__':
    input_arr = [8,7,2,5,3,1,9]
    sum = 10
    are_pair(input_arr,sum)