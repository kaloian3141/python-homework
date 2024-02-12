def is_decreasing(Arr):
    ok=1
    i=0
    while i<len(Arr)-1:
       if Arr[i]<=Arr[i+1]:
          ok=0
       i=i+1 
    return ok     
if __name__=='__main__':
    arr=[62,6,2,1]

    if is_decreasing(arr)==1:
      print("true")
    else: 
      print("false")