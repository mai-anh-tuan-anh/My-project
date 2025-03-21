def sogiomua(start,end):
    a1,b1,a2,b2=map(int,[start[0:2],start[3:],end[0:2],end[3:]])
    if(a2<a1):
        a2+=24
    elif a2==a1:
        if(b2<b1):
            a2+=24
    return float((a2*3600+b2*60-a1*3600-b1*60)/3600)
if __name__=='__main__':
    dt=dict()
    for t in range(int(input())):
        name=input()
        thoigianmua=sogiomua(input(),input())
        luongmua=float(input())
        if name not in dt:
            dt[name]=[thoigianmua,luongmua]
        else:
            dt[name][0]+=thoigianmua
            dt[name][1]+=luongmua
    i=0
    for key in dt.keys():
        i+=1
        print('T0{} {} {:.2f}'.format(i,key,dt[key][1]/dt[key][0]))
