def is_anagram(word,t):
    lst=list(word)
    lst_1=list(t)
    lst.sort()
    lst_1.sort()
    if lst==lst_1:
        return True
    else:
        return False
print(is_anagram("anagram","naagram"))
