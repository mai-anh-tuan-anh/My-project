from datetime import *
class cathi:
    def  __init__(self,macathi,ngaythi,giothi,phongthi,thoigian,songay):
        self.macathi = "C" + macathi.zfill(3)
        self.ngaythi=ngaythi
        self.giothi=giothi
        self.phongthi=phongthi
        self.thoigian=thoigian
        self.songay=songay
with open('CATHI.in','r') as file:
    content = [line.strip() for line in file if line.strip()]
    n=int(content.pop(0))
    res=[]
    for i in range(n):
        macathi=str(i+1)
        ngaythi=content.pop(0)
        giothi=content.pop(0)
        phongthi=content.pop(0)
        thoigian=int(giothi[:2])*3600+int(giothi[3:])*60
        start_date=date(1,1,1)
        end_date=date(int(ngaythi[6:]),int(ngaythi[3:5]),int(ngaythi[:2]))
        songay=end_date-start_date
        res.append(cathi(macathi,ngaythi,giothi,phongthi,thoigian,songay))
    res=sorted(res,key=lambda x:(x.songay,x.thoigian,x.macathi))
    for i in res:
        print(i.macathi,i.ngaythi,i.giothi,i.phongthi)