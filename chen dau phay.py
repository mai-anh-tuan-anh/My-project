s=input()
lst=list(s)
for i in range(len(s)-3,0,-3):
    lst.insert(i,',')
for i in range(len(lst)):
    print(lst[i],end='')