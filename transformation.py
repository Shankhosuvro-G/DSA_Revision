def transformation(word):
    lst=list(word)
    new_lst=[]
    for i in lst:
        if i=="a":
            new_lst.append("b")
        elif i=="b":
            new_lst.append("a")
    return "".join(new_lst)
print(transformation("aabb"))