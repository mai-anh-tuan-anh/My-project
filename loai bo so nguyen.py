with open('DATA.in','r') as file:
    lst=[]
    for line in file:
        lst.extend(list(line.split()))
    res=[]
    for item in lst:
        try:
            item=int(item)
            if(item>1<<63):
                res.append(str(item))
        except:
            res.append(item)
    res=sorted(res)
    print(*res)
        