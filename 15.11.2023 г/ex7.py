if __name__=='__main__':
    set1 = {1, 2, 3}
    list1 = [4, 5, 6,1]
    i = 0
    while i < len(set1):
       set1.add(list1[i])
       i += 1
    print(set1)