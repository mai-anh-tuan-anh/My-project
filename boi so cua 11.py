while True:
    x=input()
    if int(x)==-1: break
    tongle,tongchan=0,0
    for i in range(len(x)):
        if(int(i)&1): tongle+=int(x[i])
        else: tongchan+=int(x[i])    
    print('YES' if (abs(tongle-tongchan)%11==0) else 'NO')