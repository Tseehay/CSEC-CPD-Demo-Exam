n= int(input())
m=[ int(x) for x in input().split()]
sw=[]
for i in range (n):
    a=i
    for j in range(i+1,n):
        if m[j]<m[a]:
            a=j
    if i != a:
        m[i],m[a]=m[a],m[i]
        sw.append((i,a))
print(len(sw))
for k in sw:
    print(k[0],k[1])

