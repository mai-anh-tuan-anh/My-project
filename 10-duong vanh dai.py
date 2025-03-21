m=int(input())
v=int(input())
t=int(input())
d=input()
quangduong=v*t
vitri=quangduong%m
if d=='A' and not(vitri==0):
    vitri=m-vitri
print(vitri)