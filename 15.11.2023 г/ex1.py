def order(list1,list2):
    i=0
    j=len(list2)-1
    while i<len(list1):
        print(list1[i],list2[j])
        i+=1
        j-=1


if __name__=='__main__':
    list1 = [1,2,3,4]
    list2 = [5,6,7,8]
    order(list1,list2)
    