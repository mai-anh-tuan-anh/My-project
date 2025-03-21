a=[]
dt={}
for i in range(int(input())):
    s=input()
    if s!='':
        a.append(s)
        if(len(a)==1):
            dt[a[0]]=0
        else:
            dt[a[0]]+=1
    else:
        a.clear()
for key,value in dt.items():
    print(f'{key}: {value}')