from datetime import *
class thongke:
    def __init__(self,ma,ten,sophong,songay,thanhtien):
        if ma<10:
            self.ma='KH0'+str(ma)
        else:
            self.ma='KH'+str(ma)
        self.ten=ten
        self.sophong=sophong
        self.songay=songay
        self.thanhtien=thanhtien
if __name__=='__main__':
    dongia={1:25,2:34,3:50,4:80}
    nguoi=[]
    for i in range(1,int(input())+1):
        ten=input()
        sophong=input()
        tang=int(sophong)//100
        ngaynhan=input()
        ngaynhan=datetime(int(ngaynhan[6:]),int(ngaynhan[3:5]),int(ngaynhan[:2]))
        ngaytra=input()
        ngaytra=datetime(int(ngaytra[6:]),int(ngaytra[3:5]),int(ngaytra[:2]))
        songay=(ngaytra-ngaynhan).days+1
        tiendichvu=int(input())
        thanhtien= tiendichvu + dongia[tang] *songay
        nguoi.append(thongke(i,ten,sophong,songay,thanhtien))
    nguoi=sorted(nguoi,key=lambda x:-x.thanhtien)
    for i in nguoi:
        print(i.ma,i.ten,i.sophong,i.songay,i.thanhtien)