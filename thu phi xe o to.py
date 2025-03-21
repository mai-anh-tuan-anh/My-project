giatien={5:10000,7:15000,2:20000,29:50000,45:70000}
dt=dict()
for t in range(int(input())):
    bienxe,loaixe,soghe,huongdi,ngaydi=input().split()
    if huongdi=='IN':
        if(ngaydi not in dt):
            dt[ngaydi]=giatien[int(soghe)]
        else:
            dt[ngaydi]+=giatien[int(soghe)]
for key,value in dt.items():
    print(f'{key}: {value}')