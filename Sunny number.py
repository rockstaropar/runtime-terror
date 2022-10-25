a=int(input())
s = 0
temp = a
while(a>0):
    s+=((a%10))
    a//=10
print(temp == (s**2))
