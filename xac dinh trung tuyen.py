class GiaoVien:
    def __init__(self,ma,ten,monhoc,tongdiem,trangthai):
        self.ma=ma
        self.ten=ten
        self.monhoc=monhoc
        self.tongdiem=tongdiem
        self.trangthai=trangthai
if __name__=='__main__':
    diem={'1':2.0 , '2':1.5 , '3':1.0 , '4':0.0}
    mon={'A':'TOAN' , 'B':'LY' , 'C':'HOA'}
    danhsach=[]
    for i in range(1,int(input())+1):
        if i<10:
            ma='GV0'+str(i)
        else:
            ma='GV'+str(i)
        ten=input()
        maxettuyen=input()
        monhoc=mon[maxettuyen[0]]
        diemtinhoc=float(input())
        diemchuyenmon=float(input())
        diemuutien=float(diem[maxettuyen[1]])
        tongdiem=diemtinhoc*2+diemchuyenmon+diemuutien
        trangthai='TRUNG TUYEN'
        if tongdiem<18:
            trangthai='LOAI'
        danhsach.append(GiaoVien(ma,ten,monhoc,tongdiem,trangthai))
    danhsach=sorted(danhsach,key=lambda x:-x.tongdiem)
    for gv in danhsach:
        print(gv.ma,gv.ten,gv.monhoc,gv.tongdiem,gv.trangthai)