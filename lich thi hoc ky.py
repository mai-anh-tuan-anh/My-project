from datetime import *
class lichthi:
    def __init__(self,macathi,mamonhoc,monhoc,ngaythi,giothi,nhomthi,songay,thoigian):
        self.macathi='T'+macathi.zfill(3)
        self.mamonhoc=mamonhoc
        self.monhoc=monhoc
        self.ngaythi=ngaythi
        self.giothi=giothi
        self.nhomthi=nhomthi
        self.songay=songay
        self.thoigian=thoigian
if __name__=='__main__':
    n,m=map(int,input().split())
    dt={}
    for i in range(n):
        mamonhoc=input()
        monhoc=input()
        dt[mamonhoc]=monhoc
    res=[]
    for i in range(m): 
        mamonhoc,ngaythi,giothi,nhomthi=input().split()
        start_date=date(1,1,1)
        end_date=date(int(ngaythi[6:]),int(ngaythi[3:5]),int(ngaythi[:2]))
        songay=end_date-start_date
        thoigian=int(giothi[:2])*3600+int(giothi[3:])*60
        res.append(lichthi(str(i+1),mamonhoc,dt[mamonhoc],ngaythi,giothi,nhomthi,songay,thoigian))
    res=sorted(res,key=lambda x:(x.songay,x.thoigian,x.mamonhoc))
    for i in res:
        print(i.macathi,i.mamonhoc,i.monhoc,i.ngaythi,i.giothi,i.nhomthi    )