from datetime import *
class thongtin:
    def __init__(self,maphim,theloai,ngay,tenphim,sotap,songay):
        self.maphim='P'+maphim.zfill(3)
        self.theloai=theloai
        self.ngay=ngay
        self.tenphim=tenphim
        self.sotap=sotap
        self.songay=songay
n,m=map(int,input().split())
dt={}
for i in range(1,n+1):
    dt[i]=input()
res=[]
for i in range(m):
    maphim=str(i+1)
    matheloai=input()
    ngay=input()
    tenphim=input()
    sotap=int(input())
    start_date=date(1,1,1)
    end_date=date(int(ngay[6:]),int(ngay[3:5]),int(ngay[:2]))
    songay=end_date-start_date
    theloai=dt[int(matheloai[2:])]
    res.append(thongtin(maphim,theloai,ngay,tenphim,sotap,songay))
res=sorted(res,key=lambda x:(x.songay,x.tenphim,x.sotap))
for i in res:
    print(i.maphim,i.theloai,i.ngay,i.tenphim,i.sotap)