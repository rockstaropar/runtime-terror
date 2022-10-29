n=int(input())
c=0
d=0
x=n
while(x!=0):
    r=x%10
    y=n
    d=d+1
    while(y!=0):
        r1=y%10
        if(r==r1):
            c=c+1
        y=y//10
    x=x//10
if(d==c):
    print("unique number")
else:
    print("not")
