def is_anagram(name_1,name_2):
   a = 0
   if sorted(name_1)==sorted(name_2):
      a = 1
   return a


if __name__=='__main__':
    name_1 = "wor1d_"
    name_2 = "word_1"
    a=is_anagram(name_1,name_2)
    print(a)
   
