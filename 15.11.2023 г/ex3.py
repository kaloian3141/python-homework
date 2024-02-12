def a(sampledict,keys):
    i=0
    new_dict ={}
    while i<len(keys):
        if keys[i] in sampledict:
            new_dict[keys[i]]=sampledict[keys[i]] 
        i+=1
    return new_dict
if __name__=='__main__':
    sampledict = {
        "name": "A",
        "age": 1,
        "salary":2,
        "city":"NY"
    }    
    keys =["salary","age","city"]
    result = a(sampledict,keys)
    print(result)