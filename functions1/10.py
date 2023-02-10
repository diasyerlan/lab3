def unq(l):
    l.sort()
    new_l = []
    for item in l:
        if item not in new_l:
            new_l.append(item)
    print(new_l)
    
list = [1, 4, 1, 5, 6, 2]
unq(list)
    