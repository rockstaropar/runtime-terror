n=int(input())
s=0
x=n
c=0
rev=0
while(x!=0):
    r=x%10
    rev=rev*10+r
    x=x//10
while(rev!=0):
    r=rev%10
    c=c+1
    s=s+r**c
    rev=rev//10
if(s==n):
    print("disarium number")
else:
    print("not")
