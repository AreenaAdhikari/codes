def match_words(words):
    ctr = 0
    lst = []
    for word in words :
        if len(word)>1 and word[0]== word[-1]:
            ctr+= 1
            lst.append(word)
    print("list of words with same first and last character ",lst)
    return ctr
count = match_words(['acb','cfc','xyz','aba','1221'])
print("Number of words with first and last letter the same are :",count)