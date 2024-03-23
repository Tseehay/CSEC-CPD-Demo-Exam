n=int(input())
e1=0
e2=0
e3=0

for i in range(n):
    x,y,z=[int(c) for c in input().split()]
    e1+=x
    e2+=y
    e3+=z

if e1==0 and e2==0 and e3==0:
    print("YES")

else:
    print("NO")