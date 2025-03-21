class thongtin:
    def __init__(self,mathisinh,hoten,tongdiem,trangthai):
            self.mathisinh='TS'+mathisinh.zfill(2)
            self.hoten=hoten
            self.tongdiem=tongdiem
            self.trangthai=trangthai
if __name__=='__main__':
    dt={'1':1.5 , '2':1.0 , '3':0.0}
    res=[]
    for i in range(int(input())):
        hoten=' '.join(list(input().title().split()))
        diemthi=float(input())
        dantoc=input()
        khuvuc=input()
        diemthi+=dt[khuvuc]
        if dantoc!='Kinh':
            diemthi+=1.5
        trangthai='Do' if diemthi>=20.5 else 'Truot'
        res.append(thongtin(str(i+1),hoten,diemthi,trangthai))
    res=sorted(res,key=lambda x:(-x.tongdiem,x.mathisinh))
    for i in res:
        print(i.mathisinh,i.hoten,i.tongdiem,i.trangthai)