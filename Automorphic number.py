a = int(input())
temp = a
s=0
while(a>0):
    s+=((a%10)**3)
    a//=10
print(temp==s)
print(s)
