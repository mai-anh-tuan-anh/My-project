class stu:
    def __init__(self,name,lythuyet,thuchanh,maso):
        self.name=name
        if(float(lythuyet)>10):
            self.lythuyet=float(lythuyet[0]+'.'+lythuyet[1:])
        else:
            self.lythuyet=float(lythuyet)
        if(float(thuchanh)>10):
            self.thuchanh=float(thuchanh[0]+'.'+thuchanh[1:])
        else:
            self.thuchanh=float(thuchanh)
        self.maso='TS0'+str(maso)
        self.trungbinh=(self.lythuyet+self.thuchanh)/2
        if self.trungbinh<5:
            self.trangthai='TRUOT'
        elif self.trungbinh<8:
            self.trangthai='CAN NHAC'
        elif self.trungbinh<=9.5:
            self.trangthai='DAT'
        else:
            self.trangthai='XUAT SAC'
if __name__=='__main__':
    a=[]
    for i in range(1,int(input())+1):
        a.append(stu(input(),input(),input(),i))
    a=sorted(a,key=lambda x:(-x.trungbinh))
    for i in a:
        print('{} {} {:.2f} {}'.format(i.maso,i.name,i.trungbinh,i.trangthai))