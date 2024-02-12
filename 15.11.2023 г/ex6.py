def get_second_element(tuple1):
    return tuple1[1]
if __name__=='__main__':
  tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 21))
  sorted_tuple = tuple(sorted(tuple1, key=get_second_element))
  print(sorted_tuple)