def is_simetric(input_arr):
    i=0
    while i<len(input_arr):
        j=i+1
        while j<len(input_arr):
            if sorted(input_arr[i])==sorted(input_arr[j]) and input_arr[i]!=input_arr[j]:
                print(input_arr[i],input_arr[j])
            j+=1
        i+=1        
if __name__ == '__main__':
    input_arr = [[3, 4], [1, 2], [5, 2], [7, 10], [4, 3], [2, 5],[7,10]]
    is_simetric(input_arr)
