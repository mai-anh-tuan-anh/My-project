class thongtin:
    def __init__(self,makhachhang,hoten,tientrongdinhmuc,tienvuotdinhmuc,thue,tongtien):
        self.makhachhang='KH'+makhachhang.zfill(2)
        self.hoten=hoten
        self.tientrongdinhmuc=tientrongdinhmuc
        self.tienvuotdinhmuc=tienvuotdinhmuc
        self.thue=thue
        self.tongtien=tongtien
if __name__=='__main__':
    dt={'A':100 , 'B':500 , 'C':200}
    res=[]
    for i in range(int(input())):
        hoten=' '.join(list(input().title().split()))
        hogiadinh,chisodau,chisocuoi=input().split()
        sodien=int(chisocuoi)-int(chisodau)
        tientrongdinhmuc=sodien*450 if sodien<dt[hogiadinh] else dt[hogiadinh]*450
        tienvuotdinhmuc=0 if sodien<=dt[hogiadinh] else (sodien-dt[hogiadinh])*1000
        thue=tienvuotdinhmuc//20
        tongtien=tientrongdinhmuc+tienvuotdinhmuc+thue
        res.append(thongtin(str(i+1),hoten,tientrongdinhmuc,tienvuotdinhmuc,thue,tongtien))
    res=sorted(res,key=lambda x:(-x.tongtien))
    for i in res:
        print(i.makhachhang,i.hoten,i.tientrongdinhmuc,i.tienvuotdinhmuc,i.thue,i.tongtien)