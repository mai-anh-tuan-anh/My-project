class HoaDon:
    def __init__(self,ma,ten,soluong,dongia,chietkhau,tongtien):
        self.ma=ma
        self.ten=ten
        self.soluong=soluong
        self.dongia=dongia
        self.chietkhau=chietkhau
        self.tongtien=tongtien
if __name__=='__main__':
    lst=[]
    for i in range(int(input())):
        ma=input()
        ten=input()
        soluong=int(input())
        dongia=int(input())
        chietkhau=int(input())
        tongtien=soluong*dongia-chietkhau
        lst.append(HoaDon(ma,ten,soluong,dongia,chietkhau,tongtien))
    lst=sorted(lst,key=lambda x:-x.tongtien)
    for hoadon in lst:
        print(hoadon.ma,hoadon.ten,hoadon.soluong,hoadon.dongia,hoadon.chietkhau,hoadon.tongtien)