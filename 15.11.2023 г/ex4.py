if __name__=='__main__':
    sampledict ={
        "physics":53,
        "math":34,
        "history":388
    }
    min_key = None
    min_value = None

    for key, value in sampledict.items():
        if min_value is None or value < min_value:
           min_key = key
           min_value = value
    print(min_key)       