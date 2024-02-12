def permutations(list1,list2):
    list3 =[]
    i=0
    while i<len(list1):
        j=0
        while j<len(list2):
            list3.append(list1[i]+' '+list2[j])
            j+=1
        i+=1    
    return list3
if __name__=='__main__':
    list1 = ["a","b"]
    list2 = ["c","d"]
    result_list = permutations(list1,list2)
    print(result_list)