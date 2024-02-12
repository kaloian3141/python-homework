def count_words(list_of_words):
    dict_of_words = {}
    i = 0
    while i < len(list_of_words):
            word = list_of_words[i]
            if word in dict_of_words:
                dict_of_words[word] += 1
            else:
                dict_of_words[word] = 1
            i+=1    
    return dict_of_words

if __name__=='__main__':
    list_of_words = ["word1","word2","word1","word2"]
    dict_of_words = count_words(list_of_words)
    print(dict_of_words)