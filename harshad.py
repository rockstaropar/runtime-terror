n=int(input())
x=n
i=1
s=0
while(x!=0):
    r=x%10
    s=s+r
    x=x//10
if(n%s==0):
    print("harshad number")
else:
    print("not")
