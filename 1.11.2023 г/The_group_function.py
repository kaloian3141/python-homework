def group(arr):
    arr_list = []
    current_group = [arr[0]]
    i = 1
    while i<len(arr):
        current_number = arr[i]
        if current_number == arr[i - 1]:
            current_group.append(current_number)
        else:
            arr_list.append(current_group)
            current_group = [current_number]
        i += 1    

    arr_list.append(current_group)
    return arr_list

def max_consecutive(arr):
    max_count = 1
    current_count = 1
    i=1
    while i<len(arr):
        if arr[i] == arr[i - 1]:
            current_count += 1
        else:
            if current_count>max_count:
                max_count=current_count
            current_count = 1
        i += 1 
    return max_count       
    
if __name__=='__main__':
    arr = [1,1,1,2,3,4,4]
    arr_list=group(arr)
    max_count = max_consecutive(arr)
    print(arr_list,max_count)