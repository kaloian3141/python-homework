def nan_expand(number):
   i = 1
   if number < 1:
    text=""
   else:
    text = "not a "
    while i < number:
      text += "mot a "
      i += 1
    text += "NaN"
    print(text)

if __name__=='__main__':
    number = 6
    nan_expand(number)