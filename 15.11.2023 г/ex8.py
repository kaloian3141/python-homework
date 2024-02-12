if __name__=='__main__':
   set1 = {1, 2, 3, 4, 5}
   set2 = {3, 4, 5, 6, 7}
   result_set = set()
   for item in set1:
      if item in set2:
         result_set.add(item)
   print(result_set) 