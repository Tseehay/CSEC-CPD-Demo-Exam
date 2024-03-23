n = int(input())
c = 0

for i in range(n):
    a, b, c = map(int, input().split())
    
    s= a + b + c
    
    if s >= 2:
        c += 1

print(c)
